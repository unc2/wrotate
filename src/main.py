import win32api as win32api
import win32con as con

device = win32api.EnumDisplayDevices(None, 0)
dm = win32api.EnumDisplaySettings(
    device.DeviceName, con.ENUM_CURRENT_SETTINGS)

if dm.DisplayOrientation == con.DMDO_90:
    dm.DisplayOrientation = con.DMDO_DEFAULT

elif dm.DisplayOrientation == con.DMDO_DEFAULT:
    dm.DisplayOrientation = con.DMDO_90
dm.PelsWidth, dm.PelsHeight = dm.PelsHeight, dm.PelsWidth

v = win32api.ChangeDisplaySettingsEx(device.DeviceName, dm)
