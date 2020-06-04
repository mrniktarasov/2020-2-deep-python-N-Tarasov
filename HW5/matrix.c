#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <string.h>
#include <structmember.h>
#include <stdlib.h>
#include <stdio.h>
#include <malloc.h>

//что матрица содержит
typedef struct {
    PyObject_HEAD
    PyObject *matrix;
} MatrixObject;

//удаление объекта из памяти
static void Matrix_dealloc(MatrixObject *self) {
    Py_XDECREF(self -> matrix);
    Py_TYPE(self) -> tp_free((PyObject *) self);
}

//функция инициализации
static int Matrix_init(MatrixObject *self, PyObject *args, PyObject *kwds) {
    PyObject *matrix= NULL, *tmp;

    if (!PyArg_ParseTuple(args, "O", &matrix))
        return -1;
// проверка на размер

    if (matrix) {
        tmp = self -> matrix;
        Py_INCREF(matrix);
        self -> matrix = matrix;
        Py_XDECREF(tmp);
    }
    return 0;
}

//список с доступными методами
static PyMemberDef Matrix_members[] = {
    {"matrix", T_OBJECT_EX, offsetof(MatrixObject, matrix), 0,
     "list_of_lists"},
    {NULL}
};


static PyObject* add_matrix (MatrixObject* self, PyObject* args) {
    MatrixObject *other;
    if (!PyArg_ParseTuple(args, "O", &other))
        return NULL;

    long row_number = PyList_Size(self -> matrix);
    long column_number = PyList_Size(PyList_GetItem(self -> matrix, 0));
    for (long i = 0; i < row_number; i++)
        for (long j = 0; j < column_number; j++) {
            PyList_SetItem(PyList_GetItem(self -> matrix, i), j,
                    Py_BuildValue("l", PyLong_AsLong(PyList_GetItem(PyList_GetItem(self -> matrix, i), j))
                                        + PyLong_AsLong(PyList_GetItem(PyList_GetItem(other -> matrix, i), j))));
        }
    return Py_BuildValue("O", self -> matrix);
}



static PyObject* mult_matrix (MatrixObject* self, PyObject* args) {
    MatrixObject *other;

    if (!PyArg_ParseTuple(args, "O", &other))
        return NULL;

    long row_number_first = PyList_Size(self -> matrix);
    long column_number_first = PyList_Size(PyList_GetItem(self -> matrix, 0));
    long column_number_second = PyList_Size(PyList_GetItem(other -> matrix, 0));
    PyObject *row = PyList_New(0);
	PyObject *res_matrix = PyList_New(0);
	long el = 0;

    for (long i = 0; i < row_number_first; i++) {
        for (long j = 0; j < column_number_second; j++) {
            for (long k = 0; k < column_number_first; k++) {
                el += PyLong_AsLong(PyList_GetItem(PyList_GetItem(self -> matrix, i), k))*
                                        PyLong_AsLong(PyList_GetItem(PyList_GetItem(other -> matrix, k), j));
            }
            PyList_Append(row,Py_BuildValue("l", el));
			el = 0;
	    }
		PyList_Append(res_matrix, row);
		row = PyList_New(0);
	}
    return Py_BuildValue("O", res_matrix);
}


static PyObject* mult_number (MatrixObject* self, PyObject* args) {
    long n;
    if (!PyArg_ParseTuple(args, "l", &n))
        return NULL;

    long row_number = PyList_Size(self -> matrix);
    long column_number = PyList_Size(PyList_GetItem(self -> matrix,0));
    for (long i = 0; i < row_number; i++)
        for (long j = 0; j < column_number; j++) {
                PyList_SetItem(PyList_GetItem(self -> matrix,i), j,
                            Py_BuildValue("l", n * PyLong_AsLong(PyList_GetItem(PyList_GetItem(self -> matrix, i), j))));
        }
    return Py_BuildValue("O", self -> matrix);
}

static PyObject* divide_number (MatrixObject* self, PyObject* args) {
    long n;
    if (!PyArg_ParseTuple(args, "l", &n))
        return NULL;

    long row_number = PyList_Size(self -> matrix);
    long column_number = PyList_Size(PyList_GetItem(self -> matrix, 0));
    for (long i = 0; i < row_number; i++)
        for (long j = 0; j < column_number; j++) {
                PyList_SetItem(PyList_GetItem(self -> matrix,i), j,
                        Py_BuildValue("l", PyLong_AsLong(PyList_GetItem(PyList_GetItem(self -> matrix, i), j))/n));
        }
    return Py_BuildValue("O",self->matrix);
}

static PyObject* transpose (MatrixObject* self) {
    long row_number = PyList_Size(self -> matrix);
    long column_number = PyList_Size(PyList_GetItem(self -> matrix, 0));
    MatrixObject* new_matrix = (MatrixObject*)calloc(1, sizeof(MatrixObject));
    PyObject *row = PyList_New(0);
	PyObject *res_matrix = PyList_New(0);
    for (long i = 0; i < column_number; i++) {
        for (long j = 0; j < row_number; j++)
            {
                PyList_Append(row,Py_BuildValue("l",
                                PyLong_AsLong(PyList_GetItem(PyList_GetItem(self -> matrix, j), i))));
            }
        PyList_Append(res_matrix,row);
        row = PyList_New(0);
        }
    self -> matrix = res_matrix;
    return Py_BuildValue("O", self -> matrix);
}

static PyObject* contains (MatrixObject* self, PyObject* args) {
    long n;
    if (!PyArg_ParseTuple(args, "l", &n))
        return NULL;

    long row_number = PyList_Size(self -> matrix);
    long column_number = PyList_Size(PyList_GetItem(self -> matrix, 0));
    for (long i = 0; i < row_number; i++)
        for (long j = 0; j < column_number; j++) {
                if (PyLong_AsLong(PyList_GetItem(PyList_GetItem(self -> matrix, i), j)) == n)
                    return Py_True;
                else continue;
            }
    return Py_False;
}

static PyObject* get_element (MatrixObject* self, PyObject* args) {
    PyObject* coords;
    if (!PyArg_ParseTuple(args, "O", &coords))
        return NULL;
    long x = PyLong_AsLong(PyTuple_GetItem(coords, 0));
	long y = PyLong_AsLong(PyTuple_GetItem(coords, 1));
	return PyList_GetItem(PyList_GetItem(self -> matrix, x), y);
}


static PyObject* custom_str(MatrixObject* self) {
    char str_matrix[10000] = {0};
    long cnt = 0;
    long row_number = PyList_Size(self -> matrix);
    long column_number = PyList_Size(PyList_GetItem(self -> matrix, 0));
    for (long i = 0; i < row_number; i++) {
        for (long j = 0; j < column_number; j++) {
            char buf[20] = {0};
            sprintf(buf, "%ld ", PyLong_AsLong(PyList_GetItem(PyList_GetItem(self -> matrix, i), j)));
            strcat(str_matrix + cnt, buf);
            cnt += strlen(buf);
        }
        str_matrix[cnt-1] = '\n';
    }
    str_matrix[cnt-1] = '\0';
    return Py_BuildValue("s", str_matrix);
}

static PyObject* custom_repr(MatrixObject* self) {
    char repr_matrix[10000] = {0};
    long cnt = 1;
    long row_number = PyList_Size(self -> matrix);
    long column_number = PyList_Size(PyList_GetItem(self -> matrix, 0));
    repr_matrix[0] = '[';
    for (long i = 0; i < row_number; i++) {
        repr_matrix[cnt] = '[';
        cnt +=1;
        for (long j = 0; j < column_number; j++) {
            char buf[20] = {0};
            sprintf(buf, "%ld, ", PyLong_AsLong(PyList_GetItem(PyList_GetItem(self -> matrix, i), j)));
            strcat(repr_matrix + cnt, buf);
            cnt += strlen(buf);
        }
        repr_matrix[cnt-2] = ']';
        repr_matrix[cnt-1] = ',';
    }
    repr_matrix[cnt-1] = ']';
    repr_matrix[cnt] = ')';
    char full_repr_matrix[15000] = "Matrix(";

    return Py_BuildValue("s", strcat(full_repr_matrix, repr_matrix));
}

//определение методов класса MatrixType
static PyMethodDef Matrix_methods[] = {
    {"add_matrix", add_matrix, METH_VARARGS, "Returns sum of matrices"},
    {"mult_matrix", mult_matrix, METH_VARARGS, "Returns mult of matrices"},
    {"mult_number", mult_number, METH_VARARGS, "Multiplies matrix by number"},
    {"divide_number", divide_number, METH_VARARGS, "Divides matrix by number"},
    {"transpose", transpose, METH_NOARGS, "Transposes matrix"},
    {"contains", contains, METH_VARARGS, "is element in matrix"},
    {"get_element", get_element, METH_VARARGS, "access through index"},
    {NULL, NULL, 0, NULL}
};

//определение типа MatrixType
static PyTypeObject MatrixType = {
    PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "matrix.Matrix",
    .tp_doc = "Matrix objects",
    .tp_basicsize = sizeof(MatrixObject),
    .tp_itemsize = 0,
    .tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,
    .tp_new = PyType_GenericNew,
    .tp_init = (initproc) Matrix_init,
    .tp_dealloc = (destructor) Matrix_dealloc,
    .tp_members = Matrix_members,
    .tp_methods = Matrix_methods,
    .tp_repr = custom_repr,
    .tp_str = custom_str
};

static PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    .m_name = "matrix",
    .m_doc = "module matrix",
    .m_size = -1
};


PyMODINIT_FUNC PyInit_matrix(void)
{
    PyObject *m = NULL;
    if (PyType_Ready(&MatrixType) < 0)
        return NULL;
    if ((m = PyModule_Create(&module)) == NULL)
        return NULL;
    Py_XINCREF(&MatrixType);
    PyModule_AddObject(m, "Matrix", (PyObject *) &MatrixType);
    return m;
}