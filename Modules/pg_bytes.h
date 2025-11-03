#ifndef PG_BYTES_H
#define PG_BYTES_H
#include "Python.h"


typedef enum {
    PG_BSTATE_UNSURE = 0,
    PG_BSTATE_BYTES  = 1,
    PG_BSTATE_STRING = 2,
} PgBState;

typedef struct {
    PyBytesObject base;
    unsigned char pg_bstate;
} PgBytesObject;



#define PgBytes_GET_STATE(o)  (((PgBytesObject*)(o))->pg_bstate)
#define PgBytes_SET_STATE(o, s)  (((PgBytesObject*)(o))->pg_bstate = (s))

PyAPI_FUNC(PyObject*) PgBytes_FromBytes(const char *s, Py_ssize_t len, int bstate);
PyAPI_FUNC(int) PgBytes_Check(PyObject *op);
PyAPI_DATA(PyTypeObject) PgBytes_Type;

#endif