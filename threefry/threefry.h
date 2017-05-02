
#pragma once
#include <stdint.h>

typedef struct {
  uint64_t c0, c1;
} threefry_t;

threefry_t threefry(threefry_t p, threefry_t k);
double threefry_double(threefry_t *c, threefry_t *k);
