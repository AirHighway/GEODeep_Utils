import os
import gdal
# 不需要复杂的写出数据
# 只需要将坐标附上即可
# png图像可以直接修改后缀为tif来读取

# 这个是对单波段而言的


name_list = os.listdir(r"D:\_personSelf\_heao\SenseEarth2020-ChangeDetection-master\outdir\masks\test\im2")

src_root = r"D:\_personSelf\_heao\SenseEarth2020-ChangeDetection-master\outdir\masks\test\ahu_2020\2020_512_images"
read_root = r"D:\_personSelf\_heao\SenseEarth2020-ChangeDetection-master\outdir\masks\test\im2"
out_root = r"D:\_personSelf\_heao\SenseEarth2020-ChangeDetection-master\outdir\masks\test\im2_coor"


for file in name_list:
    # 读文件
    YG_dataset = gdal.Open(os.path.join(src_root, file))  # 打开文件，用这个tif图的投影信息
    YG_geotrans = YG_dataset.GetGeoTransform()  # 仿射矩阵
    # print(YG_geotrans)
    YG_proj = YG_dataset.GetProjection()  # 地图投影信息
    # print(YG_proj)

    # 读文件
    print(os.path.join(read_root, file))
    YG2_dataset = gdal.Open(os.path.join(read_root, file))  # 打开文件，用这个tif图的数值信息
    YG2_width = YG2_dataset.RasterXSize  # 栅格矩阵的列数
    YG2_height = YG2_dataset.RasterYSize  # 栅格矩阵的行数
    YG2_data = YG2_dataset.ReadAsArray(0, 0, YG2_width, YG2_height)  # 将数据写成数组，对应栅格矩阵
    b1 = YG2_data[0:YG2_height, 0:YG2_width]  # 获取第1波段
    # b2 = YG2_data[1, 0:YG2_height, 0:YG2_width]  # 获取第2波段
    # b3 = YG2_data[2, 0:YG2_height, 0:YG2_width]  # 获取第3波段

    # 创建tif文件
    driver = gdal.GetDriverByName("GTiff")
    # 这里的5，5就是创建一个5x5大小的tif，后面的5是波段数YG2_widthYG2_height
    New_YG_dataset = driver.Create(os.path.join(out_root, file), YG2_width, YG2_height, 1, gdal.GDT_Int32)
    New_YG_dataset.SetGeoTransform(YG_geotrans)
    New_YG_dataset.SetProjection(YG_proj)

    band1 = New_YG_dataset.GetRasterBand(1)
    band1.WriteArray(b1 * 1)  # 原图是整数，乘个0.1，与浮点数可以相加
    # band2 = New_YG_dataset.GetRasterBand(2)
    # band2.WriteArray(b2 * 1)
    # band3 = New_YG_dataset.GetRasterBand(3)
    # band3.WriteArray(b3 * 1)
