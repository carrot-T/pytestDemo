import binascii
from pprint import pprint

import can
import cantools
from ctypes import *

def periodic_send(msg):
    configs = [{'FChannel': 0, 'rate_baudrate': 500, 'data_baudrate': 2000, 'enable_120hm': True, 'is_fd': True},
               {'FChannel': 1, 'rate_baudrate': 500, 'data_baudrate': 2000, 'enable_120hm': True, 'is_fd': True},
               {'FChannel': 2, 'rate_baudrate': 500, 'data_baudrate': 2000, 'enable_120hm': True, 'is_fd': True},
               {'FChannel': 3, 'rate_baudrate': 500, 'data_baudrate': 2000, 'enable_120hm': True, 'is_fd': True}]
    # hwhandle = can.Bus(interface="libtosun", configs=configs, is_recv_error=False, is_include_tx=True, hwserial=b"")
    hwhandle = can.interface.Bus(interface="libtosun", configs=configs, is_recv_error=False, is_include_tx=True, hwserial=b"")
    task = hwhandle.send_periodic(msg,0.02)

    input('结束Y/N：')
    task.stop()
    hwhandle.shutdown()
    return task

def create_msg(frame_id,signals,channel=0):
    db_file_path = "D:\Projects\PycharmProjects\pytestDemo\data\EP32(Internal&E01&E02)_V5.3.1_CANFD_Network_20240305.dbc"
    db = cantools.db.load_file(db_file_path, database_format='dbc',encoding='gbk')

    db_msg = db.get_message_by_frame_id(frame_id)
    signal_dict = dict()
    for index in range(len(db_msg.signals)):
        # 获取当前报文下的信号索引对象
        signal = db_msg.signals[index]
        # 将当前信号名和dbc文件定义的默认值存储到字典中
        signal_dict[signal.name] = signal.initial

    # 更新该字典键值对的值
    signal_dict.update(signals)

    msg_data_encode = db_msg.encode(signal_dict)
    print('msg_data_encode：' + str(msg_data_encode))

    hex_str = binascii.hexlify(msg_data_encode).decode('utf-8')
    print('16进制显示：' + hex_str)

    msg_data_decode = db_msg.decode(msg_data_encode)
    # msg_decode = db_msg.decode(msg_encode)['BDCS1_PowerManageMode']
    print('msg_data_decode：' + str(msg_data_decode))

    msg = can.Message(channel=channel, arbitration_id=0x110, is_extended_id=False, is_remote_frame=False, dlc=8, data=msg_data_encode)

    return msg

# db_file_path = "D:\Projects\PycharmProjects\pytestDemo\data\EP32(Internal&E01&E02)_V5.3.1_CANFD_Network_20240305.dbc"
# db = cantools.db.load_file(db_file_path, database_format='dbc', encoding='gbk')
# db_msg = db.get_message_by_frame_id(0x110)
# print('msg_110:' + str(db_msg))
# signals_data = {'BDCS1_PowerManageMode': 6, 'BDCS1_PowerMode': 3}





cdd_file_path = 'D:\Projects\PycharmProjects\pytestDemo\data\CDCS_V1.5_20211201.cdd'
db1 = cantools.db.load_file(cdd_file_path, database_format='cdd', encoding='gbk')
did = db1.dids
print('did:' + str(did))

# # print('header_id:' + str(db_msg.header_id))
# # print('header_byte_order:' + str(db_msg.header_byte_order))
# print('frame_id:' + str(hex(db_msg.frame_id)))
# print('is_extended_frame:' + str(db_msg.is_extended_frame))
# print('is_fd:' + str(db_msg.is_fd))
# print('name:' + str(db_msg.name))
# print('length:' + str(db_msg.length))
# # print('is_container:' + str(db_msg.is_container))
# print('signals:' + str(db_msg.signals))
# print('signal_tree:' + str(db_msg.signal_tree))
# print('BDCS1_PowerManageMode_ini:' + str(db_msg.get_signal_by_name('BDCS1_PowerManageMode').initial))
# # print('signal_groups:' + str(db_msg.signal_groups))
# print('comment:' + str(db_msg.comment))
# print('send_type:' + str(db_msg.send_type))
# print('cycle_time:' + str(db_msg.cycle_time))

# # 假设这里是你的byte数据，示例为一个字节串
# byte_data = b'\x80\x00\x00\x00\x00\x00\x00\x00'
#
# # 将byte数据转换为十六进制字符串表示（可选步骤，方便查看）
# hex_data = binascii.hexlify(byte_data).decode('utf-8')
# print("十六进制数据:", hex_data)
#
#
# # 解析byte数据为信号值
# decoded_data = db_msg.decode(byte_data)
# print(decoded_data)
# # 输出解析后的信号值
# for signal_name, signal_value in decoded_data.items():
#     print(f"{signal_name}: {signal_value}")
# db_msg.signals.
# print('decode:' + str(db_msg.decode(b'\x80\x00\x00\x00\x00\x00\x00\x00')))

# d = {
# 'BDCS1_PowerManageMode': 8,
# 'BDCS1_PetToLookAfterRmd': 'No Reminder',
# 'BDCS1_PetToLookAfterFbk': 'OFF',
# 'BDCS1_PowerMode': 2,
# 'BDCS1_EnergyManagement': 'Default',
# 'BDCS1_HighBeamSt': 'Inactive',
# 'BDCS1_LowBeamSt': 'Inactive',
# 'BDCS1_AlarmMode': 'No-AntiTheft',
# 'BDCS1_HazardLampSt': 'Inactive',
# 'BDCS1_FrontLampSt': 'OFF',
# 'BDCS1_RightTurnLightSt': 'Inactive',
# 'BDCS1_LeftTurnLightSt': 'Inactive',
# 'BDCS1_BacklightStatus': 'Inactive',
# 'BDCS1_PositionLightSts': 'Inactive',
# 'BDCS1_FindCarSts': 'Inactive',
# 'BDCS1_FrontFogLampSt': 'Inactive',
# 'BDCS1_RearFogLampSt': 'Inactive',
# 'BDCS1_BrakeLightSts': 'Inactive',
# 'BDCS1_HazardSwSt': 'Inactive',
# 'BDCS1_TurnLightSW': 'OFF',
# 'BDCS1_HighBeamSW': 'OFF',
# 'BDCS1_HoodAjarSts': 'Closed',
# 'BDCS1_FMH_SetSts': 'Follow Me Closed',
# 'BDCS1_TrunkLockSts': 'Unlocked',
# 'BDCS1_HeadlampHeight_fb': 'Level 0',
# 'BDCS1_BackupLightSts': 'Inactive',
# 'BDCS1_OTAauthenSts': 'Default',
# 'BDCS1_CentralLockFbk': 'Unlocked',
# 'BDCS1_DRLSt': 'Inactive',
# 'BDCS1_Backlight_brightness_fb': 0,
# 'BDCS1_WelcomeLampModFbk': 'No active',
# 'BDCS1_MsgCounter': 0,
# 'BDCS1_Checksum': 0
# }
# print('decode:' + str(db_msg.encode(d)))


# signals_data = {'BDCS1_PowerManageMode': 8, 'BDCS1_PowerMode': 'ON'}
# msg_110 = create_msg(0x110,signals_data)
# periodic_send(msg_110)