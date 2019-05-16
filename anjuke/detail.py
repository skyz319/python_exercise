# coding=utf-8

import requests

url = "https://chengdu.anjuke.com/prop/view/A1670592947?from=filter-saleMetro&spread=filtersearch&invalid=1&position=2&kwtype=filter&now_time=1556590659"

header = {
        'User-Ageng': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X)\
                        AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'}

cookie = "aQQ_ajkguid=521F64C9-9727-27C2-7740-E8D737A7EFDE; wmda_uuid=51f32faeb009d4a484056c1d111d4efb; \
wmda_new_uuid=1; wmda_visited_projects=%3B6289197098934; isp=true; \
search_words=%E4%B8%89%E5%92%8C%E6%80%A1%E8%8B%91%7C%E6%80%80%E8%BF%9C%7C%E8%AF%BB; \
ctid=15; sessid=D475F928-DAB1-F8CC-A44C-8C60CE3E2ADD; lps=http%3A%2F%2Fwww.anjuke.com%2Fsy-city.html%7C; \
twe=2; ajk_member_captcha=ddb977720306a1e94b6ee0af3655277e; \
wmda_session_id_6289197098934=1556590479092-4edc952e-818a-41e5; browse_comm_ids=408097%7C228760%7C190432%7C856207%7C140795; \
propertys=rmmlrn-pqr60e_rneshp-pqr5yr_rmtlya-pqr5l5_rof17w-pqpt95_ro3v7g-pqps55_rh3x9n-pqi4mj_rjc5m0-pqi4k6_\
rl1uj3-pqhz7g_qzas3q-pqhym7_riwvno-pqhykj_qo64x6-pqhyjs_rioy66-pqhyhw_rjtf0o-pqhyfw_qio03r-pqhybx_rl2tnx-pqhy9q_ql5i8s-pqcr4p_rb0tmg-pqcqx8_rf9hpb-pqcqb2_rcde4e-pq4wyj_rcnxcg-pq4wvl_"

cookies = {i.split("=")[0]: i.split("=")[1] for i in cookie.split("; ")}

r = requests.get(url, headers=header, cookies=cookies)

with open("detail.html", 'w', encoding='utf-8') as f:
    f.write(r.content.decode())