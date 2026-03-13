import numpy as np
from scipy.interpolate import griddata

def grid_tec(df, resolution=0.5):
    """
    Convert scattered TEC observations into a gridded map.

    Parameters
    ----------
    df : pandas DataFrame
        Must contain columns: lat, lon, tec
    resolution : float
        Grid spacing in degrees

    Returns
    -------
    lon_grid, lat_grid, tec_grid
    """

    lon = df["lon"].values
    lat = df["lat"].values
    tec = df["tec"].values

    # Define grid
    lon_grid = np.arange(lon.min(), lon.max(), resolution)
    lat_grid = np.arange(lat.min(), lat.max(), resolution)

    lon_grid, lat_grid = np.meshgrid(lon_grid, lat_grid)

    # Interpolate scattered data
    tec_grid = griddata(
        (lon, lat),
        tec,
        (lon_grid, lat_grid),
        method="linear"
    )

    return lon_grid, lat_grid, tec_grid
