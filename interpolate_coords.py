import numpy as np
from numpy.lib.stride_tricks import as_strided


def adjacent_pairs(v):
    """
    Given a 1D numpy array `v = np.array([1, ..., n])`, return a 2D numpy array of
    adjacent pairs, `np.array([(1,2), ..., (n-1,n)])`.
    """
    s = v.shape
    d = len(s)
    assert d == 1, ValueError(f"Vector must be 1D - got a {d}D vector: shape = {s})")
    return np.vstack([v[:-1], v[1:]]).T


def interpolate_1d(v, step=0.2):
    v_adj = adjacent_pairs(v)
    d = np.diff(v_adj) / np.abs(np.diff(v_adj))
    interpolated = [np.arange(*r, diff * step) for r, diff in zip(v_adj, d)]
    return interpolated


def view_subarray(arr, row_offset, shape=(2,2)):
    assert row_offset < len(arr) - 1, ValueError("Can't take 2 row subarr at last row")
    return as_strided(arr[row_offset:,], shape=shape)


def interpolate_y_vals(interpolated_x_vals, xy_subarray):
    """
    Given a subarray e.g. `np.array([[9. , 4.6], [1. , 3. ]])`, give the polynomial
    equation `y = m*x**1 + c*x**0` (or simply `y = mx + c`).
    """
    m = (np.diff(xy_subarray[:,1]) / np.diff(xy_subarray[:,0]))[0]
    p_x, p_y = xy_subarray[0]
    c = p_y - (m * p_x)
    p = np.poly1d([m,c], variable="x")
    return p(interpolated_x_vals)

def interpolate_2d(v, x_step=0.2, concatenate=True):
    v_x, v_y = v[:, 0], v[:, 1]
    v_x_i = interpolate_1d(v_x, x_step)
    v_y_i = []
    for i in range(len(v) - 1):
        coord_subarray = view_subarray(v, i)
        y_interp = interpolate_y_vals(v_x_i[i], coord_subarray)
        v_y_i.append(y_interp)
    xy_i = [np.vstack([x,y]).T for x,y in zip(v_x_i, v_y_i)]
    if concatenate:
        # Concatenate into one single path and add the final point
        return np.vstack([np.concatenate(xy_i), v[-1, :]])
    else:
        # Add the final point to the final path and return as list of path coords
        xy_i[-1] = np.vstack([xy_i[-1], v[-1, :]])
        return xy_i
