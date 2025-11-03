#include "Python.h"
#include "pg_bytes.h"

PyTypeObject PgBytes_Type = {
    PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "pg_bytes",
    .tp_basicsize = sizeof(PgBytesObject),
    .tp_base = &PyBytes_Type,
};

int PgBytes_Check(PyObject *op)
{
    return PyObject_TypeCheck(op, &PgBytes_Type);
}