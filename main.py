from androguard.core.bytecodes.apk import APK
import win32api
import os


def ShellExecute_path(path):
    win32api.ShellExecute(0, 'open', path, '', '', 1)


def getCurrentPath():
    return os.path.dirname(os.path.realpath(__file__))


def isFile(path):
    if not os.path.exists(path):
        return False
    else:
        return True


def GetFileName(path):
    return os.path.basename(path)


def DeleteFile(path):
    os.remove(path)


def FindAPKFiles(path):
    fileList = []
    for root, subFolders, files in os.walk(path):
        for f in files:
            if f.endswith(".apk"):
                if isFile(root + os.sep + f):
                    fileList.append(root + os.sep + f)
    return fileList


def showAPKinfo(apkFile):
    apkinfo = APK(apkFile)
    # apkinfo.show()
    # print(apkinfo.get_package())
    # print(apkinfo.get_main_activity())
    # print(apkinfo.get_androidversion_code())
    # print(apkinfo.get_androidversion_name())
    # print(apkinfo.get_services())
    # print(apkinfo.get_receivers())
    # print(apkinfo.get_providers())

    file_name = GetFileName(apkFile)
    min_version = int(apkinfo.get_min_sdk_version())
    target_version = int(apkinfo.get_target_sdk_version())

    # print('min_version:' + str(min_version))
    # print('target_version:' + str(target_version))
    # print('permissions:' + str(apkinfo.get_permissions()))

    # file = open('apkinfo.txt', mode='wt', encoding='utf-8') # 파일 새로 생성
    file = open('apkinfo.txt', mode='a', encoding='utf-8') # 파일이 있을 경우 아래에 추가
    file.write('file_name:' + file_name + str('\n'))
    file.write('min_version:' + str(min_version) + str('\n'))
    file.write('target_version:' + str(target_version) + str('\n'))
    file.write('permissions:' + str(apkinfo.get_permissions()) + str('\n'))
    file.write(str('\n'))
    file.close()


if __name__ == '__main__':

    currentPath = getCurrentPath()
    fInfo = currentPath + '\\apkinfo.txt'
    if isFile(fInfo):
        DeleteFile(fInfo)

    fileList = FindAPKFiles(currentPath)
    for file in fileList:
        showAPKinfo(file)

    if isFile(fInfo):
        ShellExecute_path(fInfo)
