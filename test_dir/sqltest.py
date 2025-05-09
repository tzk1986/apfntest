import pymysql
import pandas as pd

# 数据库连接配置
db_config = {
    "host": "10.50.11.77",
    "user": "root",
    "password": "!@#$%^@2021@epfly",
    "database": "ifood_kitchen",  # 替换为你的数据库名称
    "port": 3306
}

# 查看每天排餐菜品和重量数据
query1 = """SELECT
    m.cook_date AS 日期,
    d.dish_name AS 菜名,
    m.cook_weight AS 重量,
    d.price AS 50克价格,
    d.category1 AS 大类,
    d.cook_method AS 制作方式 
FROM
    algorithm_test_dish d
    INNER JOIN algorithm_test_plan_item m ON d.id = m.dish_id
WHERE
	m.plan_id = 3 
ORDER BY
    m.cook_date;"""  # 替换为你的查询语句
 
# 每天排餐菜品的总重量和总价格
query2 = """SELECT
    m.cook_date AS 日期,
    SUM( m.cook_weight ) AS 总重量,
    SUM( ( m.cook_weight / 50 ) * d.price ) AS 总价格 
FROM
    algorithm_test_plan_item m
    INNER JOIN algorithm_test_dish d ON m.dish_id = d.id
WHERE
	m.plan_id = 3 
GROUP BY
    m.cook_date 
ORDER BY
    日期;"""  # 替换为你的查询语句
    
# 每天大类排餐的总重量
query3 = """SELECT 
    m.cook_date AS 日期,
    d.category1 AS 菜品大类,
    SUM(m.cook_weight) AS 分类总重量
FROM 
    algorithm_test_plan_item m
INNER JOIN 
    algorithm_test_dish d
ON 
    m.dish_id = d.id
WHERE
	m.plan_id = 3
GROUP BY 
    m.cook_date, d.category1  -- 按日期和大类双重分组
ORDER BY 
    日期, 菜品大类;"""  # 替换为你的查询语句
    

# 导出文件路径
output_file1 = r"d:\tangzk\py\seldom-web-testing\reports\output1.xlsx"
output_file2 = r"d:\tangzk\py\seldom-web-testing\reports\output2.xlsx"
output_file3 = r"d:\tangzk\py\seldom-web-testing\reports\output3.xlsx"
output_file4 = r"d:\tangzk\py\seldom-web-testing\reports\output4.xlsx"
output_file5 = r"d:\tangzk\py\seldom-web-testing\reports\output5.xlsx"
output_file6 = r"d:\tangzk\py\seldom-web-testing\reports\output6.xlsx"
output_all = r"d:\tangzk\py\seldom-web-testing\reports\output_all.xlsx"

# def fetch_data_and_export1():
#     """
#     查询每天排餐菜品和重量数据，并导出为 Excel 文件
#     """
#     try:
#         # 连接数据库
#         connection = pymysql.connect(**db_config)
#         print("数据库连接成功！")

#         # 执行查询
#         data = pd.read_sql(query1, connection)
#         # 根据日期字段添加星期几列
#         if '日期' in data.columns:
#             data['星期'] = pd.to_datetime(data['日期']).dt.day_name()
#         else:
#             print("警告: 数据中未找到 '排餐日期' 列，无法添加星期信息。")
        
#         # 导出为 Excel 文件
#         data.to_excel(output_file1, index=False)
#         print(f"数据已成功导出到 {output_file1}")
        

#     except Exception as e:
#         print(f"发生错误: {e}")

#     finally:
#         # 确保关闭数据库连接
#         if 'connection' in locals() and connection.open:
#             connection.close()
#             print("数据库连接已关闭。")



def fetch_data_and_export2():
    """ 
    查询每天排餐菜品的总重量和总价格，并添加人均消耗菜品重量和人均消费金额列
    """
    try:
        # 连接数据库
        connection = pymysql.connect(**db_config)
        print("数据库连接成功！")

        # 执行查询
        data = pd.read_sql(query2, connection)
        
        # 根据日期字段添加星期几列
        if '日期' in data.columns:
            data['星期'] = pd.to_datetime(data['日期']).dt.day_name()
        else:
            print("警告: 数据中未找到 '排餐日期' 列，无法添加星期信息。")

        # 预估人数映射（星期一到星期五不同）
        estimated_people = {
            "Monday": 300,
            "Tuesday": 280,
            "Wednesday": 280,
            "Thursday": 280,
            "Friday": 250,
        }

        # 添加人均消耗菜品重量和人均消费金额列
        data['预估人数'] = data['星期'].map(estimated_people)
        data['人均消耗重量'] = data['总重量'] / data['预估人数']
        data['人均消费金额'] = data['总价格'] / data['预估人数']
        
        # 导出为 Excel 文件
        data.to_excel(output_file2, index=False)
        print(f"数据已成功导出到 {output_file2}")
        

    except Exception as e:
        print(f"发生错误: {e}")

    finally:
        # 确保关闭数据库连接
        if 'connection' in locals() and connection.open:
            connection.close()
            print("数据库连接已关闭。")

def fetch_data_and_export3():
    """
    查询每天排餐菜品的总重量和总价格，并添加人均消耗菜品重量和人均消费金额列
    以及每天菜品分类占比汇总    
    """
    try:
        # 连接数据库
        connection = pymysql.connect(**db_config)
        print("数据库连接成功！")

        # 执行查询
        data = pd.read_sql(query2, connection)

        # 根据日期字段添加星期几列
        if '日期' in data.columns:
            data['星期'] = pd.to_datetime(data['日期']).dt.day_name()
        else:
            print("警告: 数据中未找到 '日期' 列，无法添加星期信息。")

        # 将星期几的英文转换为中文
        day_name_map = {
            "Monday": "星期一",
            "Tuesday": "星期二",
            "Wednesday": "星期三",
            "Thursday": "星期四",
            "Friday": "星期五",
            "Saturday": "星期六",
            "Sunday": "星期日",
        }
        data['星期'] = data['星期'].map(day_name_map)

        # 预估人数映射（星期一到星期五不同）
        estimated_people = {
            "星期一": 300,
            "星期二": 280,
            "星期三": 280,
            "星期四": 280,
            "星期五": 250,
        }

        # 添加人均消耗菜品重量和人均消费金额列
        data['预估人数'] = data['星期'].map(estimated_people)
        data['人均消耗重量'] = (data['总重量'] / data['预估人数']).round(2)
        data['人均消费金额'] = (data['总价格'] / data['预估人数']).round(2)

        # 确保总价格保留两位小数
        data['总价格'] = data['总价格'].round(2)
        
        # 标准值和浮动比例
        standard_weight = 350  # 标准人均消耗重量
        weight_tolerance = 0.02  # 浮动比例
        standard_price = 24  # 标准人均消费金额
        price_tolerance = 0.04  # 浮动比例

        # 计算人均消耗重量浮动范围和浮动值
        data['重量浮动范围'] = data.apply(
            lambda row: f"{(standard_weight * (1 - weight_tolerance)):.2f}-{(standard_weight * (1 + weight_tolerance)):.2f}",
            axis=1
        )
        data['重量浮动值'] = (data['人均消耗重量'] - standard_weight).round(2)
        data['重量是否在范围内'] = data['人均消耗重量'].apply(
            lambda x: "在范围内" if standard_weight * (1 - weight_tolerance) <= x <= standard_weight * (1 + weight_tolerance) else "超出范围"
        )

        # 计算人均消费金额浮动范围和浮动值
        data['价格浮动范围'] = data.apply(
            lambda row: f"{(standard_price * (1 - price_tolerance)):.2f}-{(standard_price * (1 + price_tolerance)):.2f}",
            axis=1
        )
        data['价格浮动值'] = (data['人均消费金额'] - standard_price).round(2)
        data['价格是否在范围内'] = data['人均消费金额'].apply(
            lambda x: "在范围内" if standard_price * (1 - price_tolerance) <= x <= standard_price * (1 + price_tolerance) else "超出范围"
        )

        
        # 查询每天菜品分类的总重量
        category_query = """SELECT 
            m.cook_date AS 日期,
            d.category1 AS 菜品大类,
            SUM(m.cook_weight) AS 分类总重量
        FROM 
            algorithm_test_plan_item m
        INNER JOIN 
            algorithm_test_dish d
        ON 
            m.dish_id = d.id
        GROUP BY 
            m.cook_date, d.category1  -- 按日期和大类双重分组
        ORDER BY 
            日期, 菜品大类;""" # 替换为你的查询语句

        category_data = pd.read_sql(category_query, connection)

        # 计算每天各分类的占比
        total_weight_per_day = category_data.groupby('日期')['分类总重量'].transform('sum')
        category_data['分类占比'] = (category_data['分类总重量'] / total_weight_per_day * 100).round(2)

        # 格式化分类占比为字符串
        category_summary = category_data.pivot(index='日期', columns='菜品大类', values='分类占比').fillna(0)
        category_summary['分类占比汇总'] = category_summary.apply(
            lambda row: "（大荤:小荤:素菜）：" + ":".join(f"{row.get(cat, 0):.2f}%" for cat in ['大荤', '小荤', '素菜']),
            axis=1
        )
        category_summary = category_summary.reset_index()[['日期', '分类占比汇总']]

        # 合并分类占比汇总到主数据
        data = pd.merge(data, category_summary, on='日期', how='left')

        # 使用 query1 查询制作方式数据
        cook_method_data = pd.read_sql(query1, connection)

        # 按日期和制作方式统计数量
        cook_method_summary = cook_method_data.groupby(['日期', '制作方式']).size().unstack(fill_value=0)

        # 格式化制作方式比例为字符串
        cook_method_summary['制作方式比例'] = cook_method_summary.apply(
            lambda row: "（炒菜机:蒸烤箱:人工）：" + ":".join(row.astype(str)), axis=1
        )
        cook_method_summary = cook_method_summary.reset_index()[['日期', '制作方式比例']]

        # 合并制作方式比例到主数据
        data = pd.merge(data, cook_method_summary, on='日期', how='left')
        
        
        # 导出为 Excel 文件
        data.to_excel(output_file3, index=False)
        print(f"数据已成功导出到 {output_file3}")

    except Exception as e:
        print(f"发生错误: {e}")

    finally:
        # 确保关闭数据库连接
        if 'connection' in locals() and connection.open:
            connection.close()
            print("数据库连接已关闭。")

# def fetch_data_and_export4():
#     """
#     查询每天排餐数据是否有同一个菜品连续两天排餐
#     并导出为 Excel 文件
#     """
#     try:
#         # 连接数据库
#         connection = pymysql.connect(**db_config)
#         print("数据库连接成功！")

#         # 执行查询
#         data = pd.read_sql(query1, connection)

#         # 根据日期字段添加星期几列
#         if '日期' in data.columns:
#             data['星期'] = pd.to_datetime(data['日期']).dt.day_name()
#         else:
#             print("警告: 数据中未找到 '日期' 列，无法添加星期信息。")

#         # 验证同一个菜品是否连续两天排餐
#         data['日期'] = pd.to_datetime(data['日期'])
#         data.sort_values(by=['菜名', '日期'], inplace=True)
#         data['连续排餐标记'] = (
#             (data['菜名'] == data['菜名'].shift(1)) &
#             (data['日期'] - data['日期'].shift(1) == pd.Timedelta(days=1))
#         ).astype(int)

#         # 导出为 Excel 文件
#         data.to_excel(output_file4, index=False)
#         print(f"数据已成功导出到 {output_file4}")

#     except Exception as e:
#         print(f"发生错误: {e}")

#     finally:
#         # 确保关闭数据库连接
#         if 'connection' in locals() and connection.open:
#             connection.close()
#             print("数据库连接已关闭。")

# def fetch_data_and_export5():

#     try:
#         # 连接数据库
#         connection = pymysql.connect(**db_config)
#         print("数据库连接成功！")

#         # 执行查询
#         data = pd.read_sql(query2, connection)

#         # 根据日期字段添加星期几列
#         if '日期' in data.columns:
#             data['星期'] = pd.to_datetime(data['日期']).dt.day_name()
#         else:
#             print("警告: 数据中未找到 '日期' 列，无法添加星期信息。")

#         # 查询每天菜品分类的总重量和数量
#         category_query = """SELECT 
#             m.cook_date AS 日期,
#             d.category1 AS 菜品大类,
#             d.category2 AS 细化分类,
#             COUNT(d.id) AS 分类数量,
#             SUM(m.cook_weight) AS 分类总重量
#         FROM 
#             algorithm_test_plan_item m
#         INNER JOIN 
#             algorithm_test_dish d
#         ON 
#             m.dish_id = d.id
#         GROUP BY 
#             m.cook_date, d.category1, d.category2
#         ORDER BY 
#             日期, 菜品大类, 细化分类;"""  # 替换为你的查询语句

#         category_data = pd.read_sql(category_query, connection)

#         # 计算每天各分类的占比
#         total_weight_per_day = category_data.groupby('日期')['分类总重量'].transform('sum')
#         category_data['分类占比'] = (category_data['分类总重量'] / total_weight_per_day * 100).round(2)
#         category_data['分类占比'] = category_data['分类占比'].astype(str) + "%"

#         # 统计每天各大类的数量和细化分类
#         category_summary = category_data.groupby('日期').apply(
#             lambda x: "；".join(
#                 f"{row['菜品大类']}({row['分类数量']}): {row['分类占比']}" for _, row in x.iterrows()
#             )
#         ).reset_index(name='分类数量和比例')

#         # 统计每个大类包含的细化分类及其数量比例
#         detailed_summary = category_data.groupby(['日期', '菜品大类', '细化分类']).apply(
#             lambda x: f"{x['细化分类'].iloc[0]}({x['分类数量'].sum()})"
#         ).reset_index(name='细化分类数量')

#         # 汇总细化分类为字符串
#         detailed_summary_grouped = detailed_summary.groupby(['日期', '菜品大类']).apply(
#             lambda x: "，".join(x['细化分类数量'])
#         ).reset_index(name='细化分类汇总')

#         # 合并分类数量和比例到主数据
#         data = pd.merge(data, category_summary, on='日期', how='left')

#         # 合并细化分类汇总到主数据
#         detailed_summary_pivot = detailed_summary_grouped.pivot(index='日期', columns='菜品大类', values='细化分类汇总')
#         for category in ['大荤', '小荤', '素菜']:
#             data[f'{category}细化分类'] = data['日期'].map(detailed_summary_pivot.get(category, {}))

#         # 导出为 Excel 文件
#         data.to_excel(output_file5, index=False)
#         print(f"数据已成功导出到 {output_file5}")

#     except Exception as e:
#         print(f"发生错误: {e}")

#     finally:
#         # 确保关闭数据库连接
#         if 'connection' in locals() and connection.open:
#             connection.close()
#             print("数据库连接已关闭。")

# def fetch_data_and_export6():

#     try:
#         # 连接数据库
#         connection = pymysql.connect(**db_config)
#         print("数据库连接成功！")

#         # 执行查询
#         data = pd.read_sql(query1, connection)

#         # 确保日期列存在并转换为 datetime 类型
#         if '日期' in data.columns:
#             data['日期'] = pd.to_datetime(data['日期'])
#         else:
#             raise KeyError("数据中未找到 '日期' 列，请检查查询结果。")

#         # 计算每个菜品在一周中的排餐次数
#         data['周数'] = data['日期'].dt.isocalendar().week  # 获取周数
#         weekly_counts = data.groupby(['周数', '菜名']).size().reset_index(name='排餐次数')

#         # 计算重复排餐次数
#         weekly_counts['重复次数'] = weekly_counts['排餐次数'] - 1
#         weekly_counts['重复次数'] = weekly_counts['重复次数'].clip(lower=0)  # 确保重复次数不为负数

#         # 计算重复比例
#         total_meals_per_week = weekly_counts.groupby('周数')['排餐次数'].transform('sum')
#         weekly_counts['重复比例'] = (weekly_counts['重复次数'] / total_meals_per_week).round(4)

#         # 合并重复比例到主数据
#         data = pd.merge(data, weekly_counts[['周数', '菜名', '重复比例']], on=['周数', '菜名'], how='left')

#         # 导出为 Excel 文件
#         data.to_excel(output_file6, index=False)
#         print(f"数据已成功导出到 {output_file6}")

#     except KeyError as e:
#         print(f"关键列缺失: {e}")
#     except Exception as e:
#         print(f"发生错误: {e}")

#     finally:
#         # 确保关闭数据库连接
#         if 'connection' in locals() and connection.open:
#             connection.close()
#             print("数据库连接已关闭。")



def fetch_all_results_and_export():
    """
    查看菜品是否连续排餐，以及菜品重复排餐比例
    查看每天排餐大类重量比例，以及细化分类数量
    执行多个查询并将结果导出到多个 Excel Sheet
    """
    try:
        # 连接数据库
        connection = pymysql.connect(**db_config)
        print("数据库连接成功！")

        # 执行查询
        data = pd.read_sql(query1, connection)

        # 确保日期列存在并转换为 datetime 类型
        if '日期' in data.columns:
            data['日期'] = pd.to_datetime(data['日期'])
        else:
            raise KeyError("数据中未找到 '日期' 列，请检查查询结果。")

        # 添加星期列
        data['星期'] = data['日期'].dt.day_name()

        # 将星期几的英文转换为中文
        day_name_map = {
            "Monday": "星期一",
            "Tuesday": "星期二",
            "Wednesday": "星期三",
            "Thursday": "星期四",
            "Friday": "星期五",
            "Saturday": "星期六",
            "Sunday": "星期日",
        }
        data['星期'] = data['星期'].map(day_name_map)

        # 验证连续排餐
        data.sort_values(by=['菜名', '日期'], inplace=True)
        data['连续排餐标记'] = (
            (data['菜名'] == data['菜名'].shift(1)) &
            (data['日期'] - data['日期'].shift(1) == pd.Timedelta(days=1))
        ).astype(int)

        # 计算重复比例
        data['周数'] = data['日期'].dt.isocalendar().week
        weekly_counts = data.groupby(['周数', '菜名']).size().reset_index(name='排餐次数')
        weekly_counts['重复次数'] = weekly_counts['排餐次数'] - 1
        weekly_counts['重复次数'] = weekly_counts['重复次数'].clip(lower=0)
        total_meals_per_week = weekly_counts.groupby('周数')['排餐次数'].transform('sum')
        weekly_counts['重复比例'] = (weekly_counts['重复次数'] / total_meals_per_week).round(4)
        data = pd.merge(data, weekly_counts[['周数', '菜名', '重复比例']], on=['周数', '菜名'], how='left')

        # 保存单独菜品的重复率和连续排餐标识
        sheet1_data = data[['日期', '星期', '菜名', '连续排餐标记', '重复比例']]
        # 确保 sheet1 中的日期只显示年月日
        sheet1_data['日期'] = pd.to_datetime(sheet1_data['日期']).dt.strftime('%Y-%m-%d')
        
        # 计算分类占比
        category_query = """SELECT 
            m.cook_date AS 日期,
            d.category1 AS 菜品大类,
            SUM(m.cook_weight) AS 分类总重量
        FROM 
            algorithm_test_plan_item m
        INNER JOIN 
            algorithm_test_dish d
        ON 
            m.dish_id = d.id
        WHERE
            m.plan_id = 3        
        GROUP BY 
            m.cook_date, d.category1
        ORDER BY 
            日期, 菜品大类;"""
        category_data = pd.read_sql(category_query, connection)
        category_data['日期'] = pd.to_datetime(category_data['日期'])
        total_weight_per_day = category_data.groupby('日期')['分类总重量'].transform('sum')
        category_data['分类占比'] = (category_data['分类总重量'] / total_weight_per_day * 100).round(2)

        # 格式化分类占比为字符串
        category_summary = category_data.pivot(index='日期', columns='菜品大类', values='分类占比').fillna(0)
        category_summary['分类占比汇总'] = category_summary.apply(
            lambda row: "（大荤:小荤:素菜）：" + ":".join(f"{row.get(cat, 0):.2f}%" for cat in ['大荤', '小荤', '素菜']),
            axis=1
        )
        category_summary = category_summary.reset_index()

        # 使用 query1 查询制作方式数据
        cook_method_data = pd.read_sql(query1, connection)

        # 按日期和制作方式统计数量
        cook_method_summary = cook_method_data.groupby(['日期', '制作方式']).size().unstack(fill_value=0)

        # 格式化制作方式比例为字符串
        cook_method_summary['制作方式比例'] = cook_method_summary.apply(
            lambda row: "（炒菜机:蒸烤箱:人工）：" + ":".join(row.astype(str)), axis=1
        )
        cook_method_summary = cook_method_summary.reset_index()[['日期', '制作方式比例']]

        # 确保日期列一致
        category_summary['日期'] = pd.to_datetime(category_summary['日期'])
        cook_method_summary['日期'] = pd.to_datetime(cook_method_summary['日期'])

        # 确保日期列只显示年月日
        data['日期'] = data['日期'].dt.strftime('%Y-%m-%d')
        category_data['日期'] = category_data['日期'].dt.strftime('%Y-%m-%d')
        category_summary['日期'] = category_summary['日期'].dt.strftime('%Y-%m-%d')
        cook_method_summary['日期'] = cook_method_summary['日期'].dt.strftime('%Y-%m-%d')

        # 合并分类占比汇总和制作方式比例到主数据
        sheet2_data = pd.merge(category_summary[['日期', '分类占比汇总']], cook_method_summary, on='日期', how='left')

        # 计算细化分类
        detailed_query = """SELECT 
            m.cook_date AS 日期,
            d.category1 AS 菜品大类,
            d.category2 AS 细化分类,
            COUNT(d.id) AS 分类数量
        FROM 
            algorithm_test_plan_item m
        INNER JOIN 
            algorithm_test_dish d
        ON 
            m.dish_id = d.id
        WHERE
            m.plan_id = 3
        GROUP BY 
            m.cook_date, d.category1, d.category2
        ORDER BY 
            日期, 菜品大类, 细化分类;"""
        detailed_data = pd.read_sql(detailed_query, connection)

        # 确保日期列是 datetime 类型
        detailed_data['日期'] = pd.to_datetime(detailed_data['日期'], errors='coerce')

        # 按日期和菜品大类分组，并汇总细化分类
        detailed_summary = detailed_data.groupby(['日期', '菜品大类']).apply(
            lambda x: "，".join(f"{row['细化分类']}({row['分类数量']})" for _, row in x.iterrows())
        ).reset_index(name='细化分类汇总')

        # 确保日期列只显示年月日
        detailed_summary['日期'] = detailed_summary['日期'].dt.strftime('%Y-%m-%d')

        # 保存细化分类汇总到单独的 Sheet
        sheet3_data = detailed_summary

        # 导出到 Excel 文件的多个 Sheet
        with pd.ExcelWriter(output_all) as writer:
            sheet1_data.to_excel(writer, sheet_name='菜品重复率与连续排餐', index=False)
            sheet2_data.to_excel(writer, sheet_name='分类比例与制作方式', index=False)
            sheet3_data.to_excel(writer, sheet_name='细化分类汇总', index=False)

        print(f"所有结果已成功导出到 {output_all}")

    except KeyError as e:
        print(f"关键列缺失: {e}")
    except Exception as e:
        print(f"发生错误: {e}")

    finally:
        # 确保关闭数据库连接
        if 'connection' in locals() and connection.open:
            connection.close()
            print("数据库连接已关闭。")
            
            
if __name__ == "__main__":
    # fetch_data_and_export2()
    fetch_data_and_export3()
    fetch_all_results_and_export()
