import argparse
import os

from indexes_traditional import *
from indexes_CCI import *
import utils

# Traditional indexes accuracy for dataset
def Traditional_Acuuracy(opt):
    # Define the list saving the accuracy
    nrmselist = []
    psnrlist = []
    ssimlist = []
    nrmseratio = 0
    psnrratio = 0
    ssimratio = 0
    imglist = utils.get_jpgs(opt.basepath)

    # Compute the accuracy
    for i in range(len(imglist)):
        # Full imgpath
        imgpath = os.path.join(opt.basepath, imglist[i])
        refimgpath = os.path.join(opt.refpath, imglist[i])
        # Compute the traditional indexes
        nrmse = NRMSE(refimgpath, imgpath)
        psnr = PSNR(refimgpath, imgpath)
        ssim = SSIM(refimgpath, imgpath)
        nrmselist.append(nrmse)
        psnrlist.append(psnr)
        ssimlist.append(ssim)
        nrmseratio = nrmseratio + nrmse
        psnrratio = psnrratio + psnr
        ssimratio = ssimratio + ssim
        print('The %dth image: nrmse: %f, psnr: %f, ssim: %f' % (i, nrmse, psnr, ssim))
    nrmseratio = nrmseratio / len(imglist)
    psnrratio = psnrratio / len(imglist)
    ssimratio = ssimratio / len(imglist)
    print('The overall results: NRMSE: %f, PSNR: %f, SSIM: %f' % (nrmseratio, psnrratio, ssimratio))

    return nrmselist, psnrlist, ssimlist, nrmseratio, psnrratio, ssimratio

# CCI indexes accuracy for dataset
def CCI_Acuuracy(opt):
    # Define the list saving the accuracy
    CNIlist = []
    CCIlist = []
    CCI_determinelist = []
    CNIratio = 0
    CCIratio = 0
    CCI_determineratio = 0
    imglist = utils.get_jpgs(opt.basepath)

    # Compute the accuracy
    for i in range(len(imglist)):
        # Full imgpath
        imgpath = os.path.join(opt.basepath, imglist[i])
        # Compute the traditional indexes
        CNI = SingleImageCNI(imgpath)
        CCI, CCI_determine = SingleImageCCI(imgpath)
        CNIlist.append(CNI)
        CCIlist.append(CCI)
        CCI_determinelist.append(CCI_determine)
        CNIratio = CNIratio + CNI
        CCIratio = CCIratio + CCI
        CCI_determineratio = CCI_determineratio + CCI_determine
        print('The %dth image: CNI: %f, CCI: %f, CCI_determine: %d' % (i, CNI, CCI, CCI_determine))
    CNIratio = CNIratio / len(imglist)
    CCIratio = CCIratio / len(imglist)
    CCI_determineratio = CCI_determineratio / len(imglist)
    print('The overall results: CNI: %f, CCI: %f, CCI_determine in [16, 20]: %f' % (CNIratio, CCIratio, CCI_determineratio))

    return CNIlist, CCIlist, CCI_determinelist, CNIratio, CCIratio, CCI_determineratio

if __name__ == "__main__":
    # ----------------------------------------
    #        Initialize the parameters
    # ----------------------------------------
    parser = argparse.ArgumentParser()
    parser.add_argument('--save', type = bool, default = False, help = 'whether to save the result lists to txt file')
    parser.add_argument('--basepath', type = str, \
        default = './mypath', \
            help = 'basepath')
    parser.add_argument('--refpath', type = str, \
        default = './zhangetal', \
            help = 'refpath')
    opt = parser.parse_args()
    print(opt)
    
    # Traditional Accuracy
    nrmselist, psnrlist, ssimlist, nrmseratio, psnrratio, ssimratio = Traditional_Acuuracy(opt)

    # CCI Accuracy
    CNIlist, CCIlist, CCI_determinelist, CNIratio, CCIratio, CCI_determineratio = CCI_Acuuracy(opt)

    if opt.save:
        utils.text_save(nrmselist, 'nrmselist.txt')
        utils.text_save(psnrlist, 'psnrlist.txt')
        utils.text_save(ssimlist, 'ssimlist.txt')
        utils.text_save(CNIlist, 'CNIlist.txt')
        utils.text_save(CCIlist, 'CCIlist.txt')
        utils.text_save(CCI_determinelist, 'CCI_determinelist.txt')
