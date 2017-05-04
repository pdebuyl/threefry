
#pragma once
#include <stdint.h>

typedef struct {
  uint64_t c0, c1;
} threefry_t;

uint64_t threefry_uint64(threefry_t *c, threefry_t *k);
threefry_t threefry(threefry_t p, threefry_t k);
double threefry_double(threefry_t *c, threefry_t *k);
