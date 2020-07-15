# QQ手势密码破解

根据储存在/data/data/com.tencent.mobileqq/shared_prefs/gesturepassword_sharepreference.xml中手势密码的hash和QQ号暴力破解手机QQ的手势密码

**gesturepassword_sharepreference.xml:**

```xml
<?xml version='1.0' encoding='utf-8' standalone='yes' ?>
<map>
    <string name="gesturepassword_gesture_pwdQQ">58E2D17B5A4D2E88B98083A89E55ED69</string>
    <int name="gesturepassword_gesture_stateQQ" value="2" />
    <boolean name="gesturepassword_appforground" value="false" />
    <boolean name="gesturepassword_locking" value="true" />
    <int name="gesturepassword_unlock_failed_type" value="1" />
    <int name="gesturepassword_unlock_failed_timeQQ" value="1" />
    <string name="gesturepassword_unlock_failed"></string>
    <int name="gesturepassword_gesture_modeQQ" value="21" />
    <string name="gesturepassword_currentuin_forplugin">QQ</string>
</map>
```

结果用0到8表示：

| 0    | 1    | 2    |
| 3    | 4    | 5    |
| 6    | 7    | 8    |

