# 补充“交办地区”，举报查询中已有交办地区，外部已办结中部分地区为空，需要根据表中“质量发生地”进行人工填入
PROVINCES = [
    '北京市', '天津市', '上海市', '重庆市', '河北省', '山西省', '辽宁省', '吉林省', '黑龙江省', '江苏省',
    '浙江省', '安徽省', '福建省', '江西省', '山东省', '河南省', '湖北省', '湖南省', '广东省', '海南省',
    '四川省', '贵州省', '云南省', '陕西省', '甘肃省', '青海省', '台湾省', '内蒙古自治区', '广西壮族自治区',
    '西藏自治区',
    '宁夏回族自治区', '新疆维吾尔自治区', '香港特别行政区', '澳门特别行政区'
]

# 定义城市到省份的映射字典
CITY_TO_PROVINCE = {
    # 直辖市
    '北京市': '北京市', '天津': '天津市', '上海市': '上海市', '重庆': '重庆市',
    # 河北省
    '石家庄': '河北省', '唐山': '河北省', '秦皇岛': '河北省', '邯郸': '河北省', '邢台': '河北省',
    '保定': '河北省', '张家口': '河北省', '承德': '河北省', '沧州': '河北省', '廊坊': '河北省', '衡水': '河北省',
    # 山西省
    '太原': '山西省', '大同': '山西省', '阳泉': '山西省', '长治': '山西省', '晋城': '山西省',
    '朔州': '山西省', '晋中': '山西省', '运城': '山西省', '忻州': '山西省', '临汾': '山西省', '吕梁': '山西省',
    # 辽宁省
    '沈阳': '辽宁省', '大连': '辽宁省', '鞍山': '辽宁省', '抚顺': '辽宁省', '本溪': '辽宁省',
    '丹东': '辽宁省', '锦州': '辽宁省', '营口': '辽宁省', '阜新': '辽宁省', '辽阳': '辽宁省',
    '盘锦': '辽宁省', '铁岭': '辽宁省', '朝阳': '辽宁省', '葫芦岛': '辽宁省',
    # 吉林省
    '长春': '吉林省', '吉林': '吉林省', '四平': '吉林省', '辽源': '吉林省', '通化': '吉林省',
    '白山': '吉林省', '松原': '吉林省', '白城': '吉林省', '延边': '吉林省',
    # 黑龙江省
    '哈尔滨': '黑龙江省', '齐齐哈尔': '黑龙江省', '鸡西': '黑龙江省', '鹤岗': '黑龙江省', '双鸭山': '黑龙江省',
    '大庆': '黑龙江省', '伊春': '黑龙江省', '佳木斯': '黑龙江省', '七台河': '黑龙江省', '牡丹江': '黑龙江省',
    '黑河': '黑龙江省', '绥化': '黑龙江省', '大兴安岭': '黑龙江省',
    # 江苏省
    '南京': '江苏省', '无锡': '江苏省', '徐州': '江苏省', '常州': '江苏省', '苏州': '江苏省',
    '南通': '江苏省', '连云港': '江苏省', '淮安': '江苏省', '盐城': '江苏省', '扬州': '江苏省',
    '镇江': '江苏省', '泰州': '江苏省', '宿迁': '江苏省',
    # 浙江省
    '杭州': '浙江省', '宁波': '浙江省', '温州': '浙江省', '嘉兴': '浙江省', '湖州': '浙江省',
    '绍兴': '浙江省', '金华': '浙江省', '衢州': '浙江省', '舟山': '浙江省', '台州': '浙江省',
    '丽水': '浙江省',
    # 安徽省
    '合肥': '安徽省', '芜湖': '安徽省', '蚌埠': '安徽省', '淮南': '安徽省', '马鞍山': '安徽省',
    '淮北': '安徽省', '铜陵': '安徽省', '安庆': '安徽省', '黄山': '安徽省', '滁州': '安徽省',
    '阜阳': '安徽省', '宿州': '安徽省', '六安': '安徽省', '亳州': '安徽省', '池州': '安徽省',
    '宣城': '安徽省',
    # 福建省
    '福州': '福建省', '厦门': '福建省', '莆田': '福建省', '三明': '福建省', '泉州': '福建省',
    '漳州': '福建省', '南平': '福建省', '龙岩': '福建省', '宁德': '福建省',
    # 江西省
    '南昌': '江西省', '景德镇': '江西省', '萍乡': '江西省', '九江': '江西省', '新余': '江西省',
    '鹰潭': '江西省', '赣州': '江西省', '吉安': '江西省', '宜春': '江西省', '抚州': '江西省',
    '上饶': '江西省',
    # 山东省
    '济南': '山东省', '青岛': '山东省', '淄博': '山东省', '枣庄': '山东省', '东营': '山东省',
    '烟台': '山东省', '潍坊': '山东省', '济宁': '山东省', '泰安': '山东省', '威海': '山东省',
    '日照': '山东省', '临沂': '山东省', '德州': '山东省', '聊城': '山东省', '滨州': '山东省',
    '菏泽': '山东省',
    # 河南省
    '郑州': '河南省', '开封': '河南省', '洛阳': '河南省', '平顶山': '河南省', '安阳': '河南省',
    '鹤壁': '河南省', '新乡': '河南省', '焦作': '河南省', '濮阳': '河南省', '许昌': '河南省',
    '漯河': '河南省', '三门峡': '河南省', '南阳': '河南省', '商丘': '河南省', '信阳': '河南省',
    '周口': '河南省', '驻马店': '河南省', '济源': '河南省',
    # 湖北省
    '武汉': '湖北省', '黄石': '湖北省', '十堰': '湖北省', '宜昌': '湖北省', '襄阳': '湖北省',
    '鄂州': '湖北省', '荆门': '湖北省', '孝感': '湖北省', '荆州': '湖北省', '黄冈': '湖北省',
    '咸宁': '湖北省', '随州': '湖北省', '恩施': '湖北省', '仙桃': '湖北省', '潜江': '湖北省',
    '天门': '湖北省', '神农架': '湖北省',
    # 湖南省
    '长沙': '湖南省', '株洲': '湖南省', '湘潭': '湖南省', '衡阳': '湖南省', '邵阳': '湖南省',
    '岳阳': '湖南省', '常德': '湖南省', '张家界': '湖南省', '益阳': '湖南省', '郴州': '湖南省',
    '永州': '湖南省', '怀化': '湖南省', '娄底': '湖南省', '湘西': '湖南省',
    # 广东省
    '广州': '广东省', '韶关': '广东省', '深圳': '广东省', '珠海': '广东省', '汕头': '广东省',
    '佛山': '广东省', '江门': '广东省', '湛江': '广东省', '茂名': '广东省', '肇庆': '广东省',
    '惠州': '广东省', '梅州': '广东省', '汕尾': '广东省', '河源': '广东省', '阳江': '广东省',
    '清远': '广东省', '东莞': '广东省', '中山': '广东省', '潮州': '广东省', '揭阳': '广东省',
    '云浮': '广东省',
    # 广西壮族自治区
    '南宁': '广西壮族自治区', '柳州': '广西壮族自治区', '桂林': '广西壮族自治区', '梧州': '广西壮族自治区',
    '北海': '广西壮族自治区',
    '防城港': '广西壮族自治区', '钦州': '广西壮族自治区', '贵港': '广西壮族自治区', '玉林': '广西壮族自治区',
    '百色': '广西壮族自治区',
    '贺州': '广西壮族自治区', '河池': '广西壮族自治区', '来宾': '广西壮族自治区', '崇左': '广西壮族自治区',
    # 海南省
    '海口': '海南省', '三亚': '海南省', '三沙': '海南省', '儋州': '海南省', '五指山': '海南省',
    '琼海': '海南省', '文昌': '海南省', '万宁': '海南省', '东方': '海南省', '定安': '海南省',
    '屯昌': '海南省', '澄迈': '海南省', '临高': '海南省', '白沙': '海南省', '昌江': '海南省',
    '乐东': '海南省', '陵水': '海南省', '保亭': '海南省', '琼中': '海南省',
    # 四川省
    '成都': '四川省', '自贡': '四川省', '攀枝花': '四川省', '泸州': '四川省', '德阳': '四川省',
    '绵阳': '四川省', '广元': '四川省', '遂宁': '四川省', '内江': '四川省', '乐山': '四川省',
    '南充': '四川省', '眉山': '四川省', '宜宾': '四川省', '广安': '四川省', '达州': '四川省',
    '雅安': '四川省', '巴中': '四川省', '资阳': '四川省', '阿坝': '四川省', '甘孜': '四川省',
    '凉山': '四川省',
    # 贵州省
    '贵阳': '贵州省', '六盘水': '贵州省', '遵义': '贵州省', '安顺': '贵州省', '毕节': '贵州省',
    '铜仁': '贵州省', '黔西南': '贵州省', '黔东南': '贵州省', '黔南': '贵州省',
    # 云南省
    '昆明': '云南省', '曲靖': '云南省', '玉溪': '云南省', '保山': '云南省', '昭通': '云南省',
    '丽江': '云南省', '普洱': '云南省', '临沧': '云南省', '楚雄': '云南省', '红河': '云南省',
    '文山': '云南省', '西双版纳': '云南省', '大理': '云南省', '德宏': '云南省', '怒江': '云南省',
    '迪庆': '云南省',
    # 西藏自治区
    '拉萨': '西藏自治区', '日喀则': '西藏自治区', '昌都': '西藏自治区', '林芝': '西藏自治区', '山南': '西藏自治区',
    '那曲': '西藏自治区', '阿里': '西藏自治区',
    # 陕西省
    '西安': '陕西省', '铜川': '陕西省', '宝鸡': '陕西省', '咸阳': '陕西省', '渭南': '陕西省',
    '延安': '陕西省', '汉中': '陕西省', '榆林': '陕西省', '安康': '陕西省', '商洛': '陕西省',
    # 甘肃省
    '兰州': '甘肃省', '嘉峪关': '甘肃省', '金昌': '甘肃省', '白银': '甘肃省', '天水': '甘肃省',
    '武威': '甘肃省', '张掖': '甘肃省', '平凉': '甘肃省', '酒泉': '甘肃省', '庆阳': '甘肃省',
    '定西': '甘肃省', '陇南': '甘肃省', '临夏': '甘肃省', '甘南': '甘肃省',
    # 青海省
    '西宁': '青海省', '海东': '青海省', '海北': '青海省', '黄南': '青海省', '海南': '青海省',
    '果洛': '青海省', '玉树': '青海省', '海西': '青海省',
    # 宁夏回族自治区
    '银川': '宁夏回族自治区', '石嘴山': '宁夏回族自治区', '吴忠': '宁夏回族自治区', '固原': '宁夏回族自治区',
    '中卫': '宁夏回族自治区',
    # 新疆维吾尔自治区
    '乌鲁木齐': '新疆维吾尔自治区', '克拉玛依': '新疆维吾尔自治区', '吐鲁番': '新疆维吾尔自治区',
    '哈密': '新疆维吾尔自治区', '昌吉': '新疆维吾尔自治区',
    '博尔塔拉': '新疆维吾尔自治区', '巴音郭楞': '新疆维吾尔自治区', '阿克苏': '新疆维吾尔自治区',
    '克孜勒苏': '新疆维吾尔自治区', '喀什': '新疆维吾尔自治区',
    '和田': '新疆维吾尔自治区', '伊犁': '新疆维吾尔自治区', '塔城': '新疆维吾尔自治区', '阿勒泰': '新疆维吾尔自治区',
    '石河子': '新疆维吾尔自治区',
    '阿拉尔': '新疆维吾尔自治区', '图木舒克': '新疆维吾尔自治区', '五家渠': '新疆维吾尔自治区',
    '北屯': '新疆维吾尔自治区', '铁门关': '新疆维吾尔自治区',
    '双河': '新疆维吾尔自治区', '可克达拉': '新疆维吾尔自治区', '昆玉': '新疆维吾尔自治区',
    '胡杨河': '新疆维吾尔自治区', '新星': '新疆维吾尔自治区',
    # 内蒙古自治区
    '呼和浩特': '内蒙古自治区', '包头': '内蒙古自治区', '乌海': '内蒙古自治区', '赤峰': '内蒙古自治区',
    '通辽': '内蒙古自治区',
    '鄂尔多斯': '内蒙古自治区', '呼伦贝尔': '内蒙古自治区', '巴彦淖尔': '内蒙古自治区', '乌兰察布': '内蒙古自治区',
    '兴安盟': '内蒙古自治区',
    '锡林郭勒盟': '内蒙古自治区', '阿拉善盟': '内蒙古自治区',
    # 其他
    '台湾': '台湾省', '香港': '香港特别行政区', '澳门': '澳门特别行政区'
}

# 县级区划到省级行政区的映射字典
COUNTY_TO_PROVINCE = {
    # 北京市
    '东城区': '北京市', '西城区': '北京市', '朝阳区': '北京市', '丰台区': '北京市', '石景山区': '北京市',
    '海淀区': '北京市', '顺义区': '北京市', '通州区': '北京市', '大兴区': '北京市', '房山区': '北京市',
    '门头沟区': '北京市', '昌平区': '北京市', '平谷区': '北京市', '密云区': '北京市', '延庆区': '北京市',

    # 辽宁省
    '太和区': '辽宁省', '金城江区': '辽宁省', '红旗区': '辽宁省', '牧野区': '辽宁省', '卫滨区': '辽宁省',

    # 广西壮族自治区
    '宜州区': '广西壮族自治区', '金城江区': '广西壮族自治区', '环江毛南族自治县': '广西壮族自治区',
    '巴马瑶族自治县': '广西壮族自治区',
    '平果县': '广西壮族自治区', '长洲区': '广西壮族自治区', '大化瑶族自治县': '广西壮族自治区',

    # 四川省
    '通江县': '四川省', '邛崃市': '四川省', '九台区': '四川省', '武胜县': '四川省', '邻水县': '四川省',
    '苍溪县': '四川省', '都江堰市': '四川省', '三台县': '四川省', '达川区': '四川省', '双流区': '四川省',

    # 河南省
    '红旗区': '河南省', '牧野区': '河南省', '卫滨区': '河南省', '辉县市': '河南省', '浉河区': '河南省',
    '魏都区': '河南省', '华龙区': '河南省', '中原区': '河南省', '建安区': '河南省', '桃城区': '河南省',

    # 山东省
    '东昌府区': '山东省', '台儿庄区': '山东省', '博山区': '山东省', '沂源县': '山东省', '定远县': '山东省',

    # 安徽省
    '金寨县': '安徽省', '舒城县': '安徽省', '东至县': '安徽省', '祁门县': '安徽省', '旌德县': '安徽省',
    '广德市': '安徽省', '当涂县': '安徽省', '岳西县': '安徽省', '宿城区': '安徽省', '宣州区': '安徽省',

    # 广东省
    '荔湾区': '广东省', '江南区': '广东省', '石狮市': '广东省', '邛崃市': '广东省', '樟树市': '广东省',
    '兴宁市': '广东省', '五华县': '广东省', '惠来县': '广东省', '越秀区': '广东省', '虎门镇': '广东省',

    # 其他省份
    '介休市': '山西省', '云阳县': '重庆市', '上杭县': '福建省', '庆城县': '甘肃省', '贞丰县': '贵州省',
    '利辛县': '安徽省', '漳平市': '福建省', '翁牛特旗': '内蒙古自治区', '恭城瑶族自治县': '广西壮族自治区',
    '中方县': '湖南省', '平南县': '广西壮族自治区', '洱源县': '云南省', '桂阳县': '湖南省', '巫山县': '重庆市',
    '尤溪县': '福建省', '息烽县': '贵州省', '城口县': '重庆市', '常熟市': '江苏省', '武夷山市': '福建省',
    '榕江县': '贵州省', '扶风县': '陕西省', '资兴市': '湖南省', '延津县': '河南省', '绥江县': '云南省',
    '石阡县': '贵州省', '岚县': '山西省', '巩义市': '河南省', '兴县': '山西省', '遂平县': '河南省',
    '建水县': '云南省', '晋江市': '福建省', '潞州区': '山西省', '平舆县': '河南省', '盈江县': '云南省',
    '广昌县': '江西省', '宜秀区': '安徽省', '云龙县': '云南省', '万秀区': '广西壮族自治区', '靖宇县': '吉林省',
    '昭化区': '四川省', '如皋市': '江苏省', '东胜区': '内蒙古自治区', '景谷傣族彝族自治县': '云南省',
    '桥西区': '河北省', '渝北区': '重庆市', '武隆区': '重庆市', '浈江区': '广东省', '北塔区': '湖南省',
    '肃南裕固族自治县': '甘肃省', '伊金霍洛旗': '内蒙古自治区', '喜德县': '四川省', '察哈尔右翼中旗': '内蒙古自治区',
    '宁城县': '内蒙古自治区', '杭锦后旗': '内蒙古自治区', '经济技术开发区': '河南省', '城乡一体化示范区': '河南省',
    '建安区': '河南省', '抚宁区': '河北省', '高新技术产业开发区': '安徽省', '大祥区': '湖南省',
    '冷水滩区': '湖南省', '零陵区': '湖南省', '双清区': '湖南省', '兴隆台区': '辽宁省', '山海关区': '河北省',
    '海港区': '河北省', '大观区': '安徽省', '三都水族自治县': '贵州省', '宝清县': '黑龙江省',
    '建平县': '辽宁省', '大姚县': '云南省', '田东县': '广西壮族自治区', '花山区': '安徽省', '良庆区': '广西壮族自治区',
    '新华区': '河北省', '梅江区': '广东省', '蕲春县': '湖北省', '霞浦县': '福建省', '通江县': '四川省',
    '市辖区': '', '中国': '',
    # 山西省
    '盂县': '山西省',

    # 安徽省
    '迎江区': '安徽省',
    '金安区': '安徽省',

    # 广西壮族自治区
    '西林县': '广西壮族自治区',
    '天峨县': '广西壮族自治区',
    '东兴市': '广西壮族自治区',

    # 新疆维吾尔自治区
    '温泉县': '新疆维吾尔自治区',

    # 河南省
    '睢县': '河南省',
    '滑县': '河南省',
    '金水区': '河南省',

    # 西藏自治区
    '桑珠孜区': '西藏自治区',

    # 上海市
    '浦东新区': '上海市',

    # 吉林省
    '梅河口市': '吉林省',
    '大安市': '吉林省',

    # 云南省
    '泸西县': '云南省',

    # 四川省
    '利州区': '四川省',

    # 广东省
    '金平苗族瑶族傣族自治县': '广东省',

    # 辽宁省
    '古塔区': '辽宁省',

    # 黑龙江省
    '富锦市': '黑龙江省',

    # 河北省
    '冀州区': '河北省',
    # 浙江省
    '天峨县': '广西省',
    '睢县': '河南省',
    '金湾区': '广东省',
    '香洲区': '广东省',
    '泸西县': '云南省',
    '汾阳市': '山西省',
    '南召县': '河南省',
    '东兴市': '广西省',
    '梅河口市': '吉林省',
    '南大街': '山西省',
    '大安市': '吉林省',
    '斗门区': '广东省',
    '冀州区': '河北省',
    '滑县': '河南省',
    '古塔区': '辽宁省',
    '桑珠孜区': '西藏自治区',
    '浦东新区': '上海市',
    '利州区': '四川省',
    '金平苗族瑶族傣族自治县': '贵州省',
    '冀州区': '河北省',
    '富锦市': '黑龙江省',
    '东兴市': '广西省',
    '大安市': '吉林省',
    '金水区': '河南省',
    '金安区': '安徽省',
    '金水区': '河南省',
    '金平苗族瑶族傣族自治县': '贵州省',
    '金水区': '河南省',
    '南万达': '山西省',
    '上海': '上海市',
    '青旅国际': '吉林省',
    '万达': '北京市',
    '郑州市': '河南省',
    '贵阳': '贵州省',
    '广州': '广东省',
    '重庆': '重庆市',
    '济南': '山东省',
    '金湾区': '广东省', '香洲区': '广东省', '斗门区': '广东省', '河津市': '山西省',
    '古交市': '山西省', '榆次区': '山西省', '云冈区': '山西省', '南召县': '河南省',
    '沈阳市': '辽宁省', '济南': '山东省', '昆明': '云南省', '无锡市': '江苏省',
    '临汾市': '山西省', '大安市': '吉林省', '盐城市': '江苏省', '郑州市': '河南省',
    '太原': '山西省', '南通市': '江苏省', '武汉市': '湖北省', '湘潭': '湖南省',
    '哈尔滨': '黑龙江省', '合肥': '安徽省', '深圳': '广东省', '石家庄': '河北省',
    '北京': '北京市', '江北区': '重庆市'
}

KEYWORDS = {
    # （1）文化市场
    '文化': {
        '歌舞娱乐场所': {
            '违规接纳未成年人': ['未成年人', '身份证核验'],
            '超时经营': ['超时营业', '凌晨营业'],
            '无证经营': ['无许可证', '无资质'],
            '安全': ['无消防通道', '安保'],
            '其他违规经营': ['有陪侍人员', '工作人员态度']
        },
        '互联网上网服务营业场所': {
            '违规接纳未成年人': ['未成年人', '身份证核验'],
            '无证经营': ['无许可证', '无资质'],
            '超时经营': ['超时营业', '凌晨营业'],
            '安全': ['消防', '安保'],
            '其他违规经营': ['网吧服务问题']
        },
        '演出场所经营单位、演出经纪机构、文化表演团体': {
            '擅自从事营业性演出': ['未经批准从事营业性演出', '未报批', '未备案'],
            '演出含禁止内容': ['禁止内容', '违规内容'],
            '演出活动票务问题': ['违规售票', '票务'],
            '违规经营': ['假唱欺骗观众'],
            '其他违规经营': ['非不可抗力终止演出', '内容变更未及时告知观众']
        },
        '游艺娱乐场所': {
            '违规接纳未成年人': ['未成年人', '身份证核验'],
            '违规经营': ['无许可证', '无资质'],
            '涉嫌赌博': ['赌博', '涉赌'],
            '设置未经文化部门内容核查的游戏游艺设备': ['违规放置游戏机'],
            '安全': ['消防', '安保'],
            '其他违规经营': ['机器故障', '无标识']
        },
        '互联网文化单位': {
            '含禁止内容': ['禁止内容', '血腥', '暴力'],
            '无证经营': ['无《网络文化经营许可证》', '平台擅自组织营业性演出'],
            '其他违规经营': ['组织未成年人直播']
        },
        '社会艺术水平考级机构': {
            '违规组织等级考试': ['无资质', '颁发假证']
        },
        '艺术品经营单位': {
            '向消费者隐瞒艺术品来源，或者在艺术品说明中隐瞒重要事项，误导消费者': ['伪造', '仿冒', '假货'],
            '伪造、变造或者冒充他人名义的艺术品': ['伪造', '仿冒', '假货'],
            '含禁止内容': ['含对未成年人不利', '违背正确价值观内容']
        },
        '网络表演经纪机构': {
            '无证经营': ['无《营业性演出许可证》']
        },
        '个体演员': {
            '擅自从事营业性演出': ['未经批准从事营业性演出', '未报批', '未备案'],
            '演出含禁止内容': ['禁止内容', '违规内容']
        },
        '其他娱乐场所': {
            '违规接纳未成年人': ['未成年人', '身份证核验'],
            '无证经营': ['无许可证', '无资质']
        }
    },

    # （2）旅游市场
    '旅游': {
        '旅行社、旅行社分社、旅行社服务网点': {
            '擅自变更旅游行程': ['未经游客同意行程变更', '自行更改行程', '行程与合同不符'],
            '不合理低价游': ['不合理的低价', '安排购物', '另行收费'],
            '虚假宣传误导游客': ['虚假宣传', '欺诈', '诱骗'],
            '交通、住宿、餐饮、景区等服务企业不具备接待能力': ['交通', '住宿', '餐饮条件恶劣', '不达标准'],
            '未经旅游者的同意，将旅游者转交给其他旅行社组织、接待': ['转交其他旅行社', '拼团', '转团'],
            '无证经营，出借、出租非法转让许可证': ['无证', '非法转让', '许可证', '资质'],
            '未签订旅游合同': ['未签订', '无合同'],
            '危害游客安全': ['危害游客安全', '不安全服务'],
            '其他': ['违规收取费用', '不合理收费']
        },
        '在线旅游经营活动': {
            '擅自变更旅游行程': ['未经游客同意行程变更', '自行更改行程', '行程与合同不符'],
            '不合理低价游': ['不合理的低价', '安排购物', '另行收费'],
            '虚假宣传误导游客': ['虚假宣传', '欺诈', '诱骗'],
            '未签订旅游合同': ['未签订', '无合同'],
            '未经旅游者的同意，将旅游者转交给其他旅行社组织、接待': ['转交其他旅行社', '拼团', '转团'],
            '无证经营，出借、出租、非法转让许可证': ['无证', '非法转让', '许可证', '资质']
        },
        '导游、相关人员': {
            '擅自安排购物活动、另行付费旅游活动': ['安排购物', '兜售', '另行收费', '索要消费'],
            '强制购物': ['诱骗', '欺骗', '强迫购物'],
            '无证上岗 、未佩戴导游证': ['无证', '未佩戴导游证'],
            '危及游客人身安全': ['辱骂', '恐吓', '精神伤害'],
            '拒绝履行服务': ['无讲解', '介绍', '行程通知']
        },
        '其他旅游经营活动': {
            '景区经营': ['强制收费', '无证经营', '景区服务'],
            '无证经营': ['无证', '无许可', '超范围'],
            '交通经营': ['船', '车', '停车', '司机服务'],
            '住宿经营': ['入住', '客房服务', '退房', '设施服务'],
            '餐饮经营': ['食品不达标', '食物中毒', '超范围经营'],
            '其他': ['娱乐', '购物', '违规经营']
        }
    },

    # （3）出版
    '出版': {
        '出版物经营单位': {
            '未经许可擅自从事出版业务': ['无许可', '无资质'],
            '假冒、伪造出版单位名称发行出版物': ['盗版', '伪造', '假冒', '著作权', '商标'],
            '出版物含禁止内容': ['禁止内容', '非法内容'],
            '未履行手续擅自复制境外出版物': ['非法进口'],
            '其他': ['出版物纸张质量', '服务问题']
        },
        '互联网出版机构': {
            '未经许可擅自从事出版业务': ['无许可', '无资质'],
            '假冒、伪造出版单位名称发行出版物': ['盗版', '伪造', '假冒', '侵权'],
            '出版物含禁止内容': ['禁止内容', '非法内容'],
            '其他': ['无实名认证']
        },
        '印刷企业': {
            '未经许可擅自从事复制、印刷业务': ['盗版印刷'],
            '印刷、复制禁止内容出版物': ['禁止内容复制']
        }
    },

    # （4）电影
    '电影': {
        '电影发行放映场所': {
            '未经许可发行、放映、送展电影': ['无许可', '非法放映'],
            '违规放映': ['违规放映', '含禁止内容'],
            '影院、影片侵权': ['盗版', '侵权'],
            '其他': ['刷票房', '票房数据造假']
        }
    },

    # （5）广播电视
    '广播电视': {
        '卫星传送的境外电视节目接收单位': {
            '单位、个人擅自安装和使用卫星地面接收设施': ['擅自安装', '卫星']
        },
        '广播电台电视台': {
            '擅自设立广播电台电视台、播放非法节目、未经批准擅自进口境外节目、设施破坏无非播放': ['黑广播', '非法节目',
                                                                                              '擅自播放']
        },
        '互联网视听节目服务单位': {
            '涉嫌擅自从事互联网视听节目服务、链接非法节目、含禁止内容': ['擅自从事', '非法节目', '禁止内容']
        }
    },

    # （6）文物
    '文物': {
        '文物保护单位': {
            '擅自建设工程、擅自拆除/修缮文物、盗窃文物、超范围经营、无资质运营': ['擅自建设', '擅自拆除', '盗窃文物',
                                                                              '超范围经营', '无资质运营']
        },
        '文物经营单位': {
            # 此部分暂时为空，根据实际情况补充
        },
        '文物收藏单位': {
            # 此部分暂时为空，根据实际情况补充
        }
    },

    # （7）其他
    '其他': {
        '酒吧、俱乐部等其他场所违规运营': {
            '无证经营': ['无许可证', '无资质'],
            '侵权问题': ['字体', '肖像', '侵权'],
            '违规接纳未成年人': ['未成年人', '身份证核验'],
            '超时经营': ['超时营业', '凌晨营业'],
            '其他违规运营': ['违规售票']
        }
    }
}
MARKET_CAT_DICT = {'文化': '文化',
                   '旅游': '旅游',
                   '出版': '其他',
                   '电影': '其他',
                   '广播电视': '其他',
                   '文物': '其他',
                   '其他': '其他'}
