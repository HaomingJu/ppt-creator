#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import aiohttp
import asyncio
import time
import lxml.html

RN_AUCPOINT = ["会阴穴", "曲骨穴", "中极穴", "关元穴", "石门穴", "气海穴", "阴交穴", "神阙穴", "水分穴", "下脘穴", "建里穴", "中脘穴", "上脘穴", "巨阙穴", "鸠尾穴", "中庭穴", "膻中穴", "玉堂穴", "紫宫穴", "华盖穴", "璇玑穴", "天突穴", "廉泉穴", "承浆穴"]


# 手太阴肺经
LU_AUCPOINT = ["中府穴", "云门穴", "天府穴",  "侠白穴",  "尺泽穴",  "孔最穴",  "列缺穴",  "经渠穴",  "太渊穴",  "鱼际穴", "少商穴"]

# 手阳明大肠经

LI_AUCPOINT = ["商阳穴", "二间穴", "三间穴", "合谷穴", "阳溪穴" "偏历穴", "温溜穴", "下廉穴", "上廉穴", "手三里穴", "曲池穴", "肘髎穴", "手五里穴", "臂臑穴", "肩髃穴", "巨骨穴", "天鼎穴", "扶突穴", "口禾髎穴", "迎香穴"]

# 足阳明胃经
ST_ACUPOINT = ["承泣穴", "四白穴", "巨髎穴", "地仓穴", "大迎穴", "颊车穴", "下关穴", "头维穴", "人迎穴", "水突穴", "气舍穴", "缺盆穴", "气户穴", "库房穴", "屋翳穴", "膺窗穴", "乳中穴", "乳根穴", "不容穴", "承满穴", "梁门穴", "关门穴", "太乙穴", "滑肉门穴", "天枢穴", "外陵穴", "大巨穴", "水道穴", "归来穴", "气冲穴", "髀关穴", "伏兔穴", "阴市穴", "梁丘穴", "犊鼻穴", "足三里穴", "上巨虚穴", "条口穴", "下巨虚穴", "丰隆穴", "解溪穴", "冲阳穴", "陷谷穴","内庭穴","厉兑穴"]

# 足太阴脾经Spleen Meridian of Foot-Taiyin，SP
SP_ACUPOINT = ["隐白穴", "大都穴", "太白穴", "公孙穴", "商丘穴", "三阴交穴", "漏谷穴", "地机穴", "阴陵泉穴", "血海穴", "箕门穴", "冲门穴", "府舍穴", "腹结穴", "大横穴", "腹哀穴", "食窦穴", "天溪穴", "胸乡穴", "周荣穴", "大包穴"]

# 手少阴心经Heart Meridian of Hand-shaoyin，HT
HT_ACUPOINT = ["极泉穴", "青灵穴", "少海穴", "灵道穴", "通里穴", "阴郄穴", "神门穴", "少府穴", "少冲穴"]

# 手太阳小肠经Small Instestine Meridian of Hand-Taiyang，SI
SI_ACUPOINT = ["少泽穴", "前谷穴", "后溪穴", "腕骨穴", "阳谷穴", "养老穴", "支正穴", "小海穴", "肩贞穴", "臑俞穴", "天宗穴", "秉风穴", "曲垣穴", "肩外俞穴", "肩中俞穴", "天窗穴", "天容穴", "颧髎穴", "听宫穴"]

#足太阳膀胱经，（BL，Bladder Meridian of Foot-Taiyang
BL_ACUPOINT = ["睛明穴", "攒竹穴", "眉冲穴", "曲差穴", "五处穴", "承光穴", "通天穴", "络却穴", "玉枕穴", "天柱穴", "大杼穴", "风门穴", "肺俞穴", "厥阴俞穴", "心俞穴", "督俞穴", "膈俞穴", "肝俞穴", "胆俞穴", "脾俞穴", "胃俞穴", "三焦俞穴", "肾俞穴", "气海俞穴", "大肠俞穴", "关元俞穴", "小肠俞穴", "膀胱俞穴", "中膂俞穴", "白环俞穴", "上髎穴", "次髎穴", "中髎穴", "下髎穴", "会阳穴", "承扶穴", "殷门穴", "浮郄穴", "委阳穴", "委中穴", "附分穴", "魄户穴", "膏肓穴", "神堂穴", "譩嘻穴", "膈关穴", "魂门穴", "阳纲穴", "意舍穴", "胃仓穴", "肓门穴", "志室穴", "胞肓穴", "秩边穴", "合阳穴", "承筋穴", "承山穴", "飞扬穴", "跗阳穴", "昆仑穴", "仆参穴", "申脉穴", "金门穴", "京骨穴", "束骨穴", "足通谷穴", "至阴穴"]

# 足少阴肾经 (Kidney Meridian of Foot-shaoyin，KI)
KI_ACUPOINT = ["涌泉穴", "然谷穴", "太溪穴", "大钟穴", "水泉穴", "照海穴", "复溜穴", "交信穴", "筑宾穴", "阴谷穴", "横骨穴", "大赫穴", "气穴穴", "四满穴", "中注穴", "肓俞穴", "商曲穴", "石关穴", "阴都穴", "腹通谷穴", "幽门穴", "步廊穴", "神封穴", "灵墟穴", "神藏穴", "彧中穴", "俞府穴"]


# 手厥阴心包经 Pericardium Meridian of Hand-Jueyin，PC
PC_ACUPOINT = ["天池穴", "天泉穴", "曲泽穴", "郄门穴", "间使穴", "内关穴", "大陵穴", "劳宫穴", "中冲穴"]

# 手少阳三焦经（Sanjiao Meridian of Hand-shaoyang，SJ
SJ_ACUPOINT = ["关冲穴", "液门穴", "中渚穴", "阳池穴", "外关穴", "支沟穴", "会宗穴", "三阳络穴", "四渎穴", "天井穴", "清冷渊穴", "消泺穴", "臑会穴", "肩髎穴", "天髎穴", "天牖穴", "翳风穴", "瘛脉穴", "颅息穴", "角孙穴", "耳门穴", "耳和髎穴", "丝竹空穴"]

# 足少阳胆经Gallbladder Meridian of Foot-Shaoyang，GB

GB_ACUPOINT = ["瞳子髎穴", "听会穴", "上关穴", "颔厌穴", "悬颅穴", "悬厘穴", "曲鬓穴", "率谷穴", "天冲穴", "浮白穴", "头窍阴穴", "完骨穴", "本神穴", "阳白穴", "头临泣穴", "目窗穴", "正营穴", "承灵穴", "脑空穴", "风池穴", "肩井穴", "渊腋穴", "辄筋穴", "日月穴", "京门穴", "带脉穴", "五枢穴", "维道穴", "居髎穴", "环跳穴", "风市穴", "中渎穴", "膝阳关穴", "阳陵泉穴", "阳交穴", "外丘穴", "光明穴", "阳辅穴", "悬钟穴", "丘墟穴", "足临泣穴", "地五会穴", "侠溪穴", "足窍阴穴"]

# 足厥阴肝经（Liver Meridian of Foot-Jueyin，LR
LR_ACUPOINT = ["大敦穴", "行间穴", "太冲穴", "中封穴", "蠡沟穴", "中都穴", "膝关穴", "曲泉穴", "阴包穴", "足五里穴", "阴廉穴", "急脉穴", "章门穴", "期门穴"]


async def get_acupoint_info(acupoint: str):
    async with aiohttp.ClientSession() as session:
        print("https://www.yixue.com/针灸学/{}".format(acupoint))
        async with session.get('https://www.yixue.com/针灸学/{}'.format(acupoint)) as response:
            print("------------------------ {} -----------------------".format(acupoint))
            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])
            html_text = await response.text()

            # 数据筛选
            selector = lxml.html.fromstring(html_text)

            ## 定位
            node_localization = selector.xpath('//*[@id="mw-content-text"]/div/p[1]')[0]
            info_localization = node_localization.xpath('string(.)')

            ## 解剖
            node_dissection = selector.xpath('//*[@id="mw-content-text"]/div/p[2]')[0]
            info_dissection = node_dissection.xpath('string(.)')

            ## 治疗
            node_cure = selector.xpath('//*[@id="mw-content-text"]/div/p[3]')[0]
            info_cure = node_cure.xpath('string(.)')

            ## 配伍
            node_company = selector.xpath('//*[@id="mw-content-text"]/div/p[4]')[0]
            info_company = node_company.xpath('string(.)')

            ## 针灸
            node_acupuncture = selector.xpath('//*[@id="mw-content-text"]/div/p[5]')[0]
            info_acupuncture = node_acupuncture.xpath('string(.)')
            
            print("{}:{}\n{}{}{}{}".format(acupoint, info_localization, info_dissection, info_cure, info_company , info_acupuncture))

            with open('{}.txt'.format(acupoint), 'w') as html_filehandler:
                html_filehandler.write("https://www.yixue.com/针灸学/{}\n\n{}{}{}{}{}\nhttps://www.yixue.com/{}\n".
                                       format(acupoint, info_localization, info_dissection, info_cure, info_company, info_acupuncture, acupoint))


async def main():
    cores_func = [get_acupoint_info(i) for i in LR_ACUPOINT ]
    await asyncio.gather(*cores_func)

startTime = time.time()

asyncio.run(main())

endTime = time.time()
print("总耗时: ", endTime - startTime)

