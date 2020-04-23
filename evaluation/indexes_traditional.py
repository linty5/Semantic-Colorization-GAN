from skimage import io
from skimage import measure
from skimage import transform
from skimage import color

# Compute the mean-squared error between two images
def MSE(srcpath, dstpath, scale = 256):
    scr = io.imread(srcpath)
    dst = io.imread(dstpath)
    scr = transform.resize(scr, (scale, scale))
    dst = transform.resize(dst, (scale, scale))
    mse = measure.compare_mse(scr, dst)
    return mse

# Compute the normalized root mean-squared error (NRMSE) between two images
def NRMSE(srcpath, dstpath, mse_type = 'Euclidean', scale = 256):
    scr = io.imread(srcpath)
    dst = io.imread(dstpath)
    scr = transform.resize(scr, (scale, scale))
    dst = transform.resize(dst, (scale, scale))
    nrmse = measure.compare_nrmse(scr, dst, norm_type = mse_type)
    return nrmse

# Compute the peak signal to noise ratio (PSNR) for an image
def PSNR(srcpath, dstpath, scale = 256):
    scr = io.imread(srcpath)
    dst = io.imread(dstpath)
    scr = transform.resize(scr, (scale, scale))
    dst = transform.resize(dst, (scale, scale))
    psnr = measure.compare_psnr(scr, dst)
    return psnr

# Compute the mean structural similarity index between two images
def SSIM(srcpath, dstpath, RGBinput = True, scale = 256):
    scr = io.imread(srcpath)
    dst = io.imread(dstpath)
    scr = transform.resize(scr, (scale, scale))
    dst = transform.resize(dst, (scale, scale))
    ssim = measure.compare_ssim(scr, dst, multichannel = RGBinput)
    return ssim
