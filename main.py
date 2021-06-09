from androguard.core.bytecodes.apk import APK
import win32api


def ShellExecute_path(path):
    win32api.ShellExecute(0, 'open', path, '', '', 1)


if __name__ == '__main__':
    apkFile = 'app-release.apk'
    apkinfo = APK(apkFile)
    # apkinfo.show()
    # print(apkinfo.get_package())
    # print(apkinfo.get_main_activity())
    # print(apkinfo.get_androidversion_code())
    # print(apkinfo.get_androidversion_name())
    # print(apkinfo.get_services())
    # print(apkinfo.get_receivers())
    # print(apkinfo.get_providers())

    min_version = int(apkinfo.get_min_sdk_version())
    target_version = int(apkinfo.get_target_sdk_version())

    # print('min_version:' + str(min_version))
    # print('target_version:' + str(target_version))
    # print('permissions:' + str(apkinfo.get_permissions()))

    file = open('apkinfo.txt', mode='wt', encoding='utf-8')
    file.write('min_version:' + str(min_version) + str('\n'))
    file.write('target_version:' + str(target_version) + str('\n'))
    file.write('permissions:' + str(apkinfo.get_permissions()) + str('\n'))
    file.close()

    ShellExecute_path('apkinfo.txt')
