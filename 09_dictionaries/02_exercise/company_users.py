dict_companies_ids = {}
company_id_data = input().split(" -> ")
while company_id_data[0] != 'End':
    company_name, employee_id = company_id_data[0], company_id_data[1]
    if company_name not in dict_companies_ids:
        dict_companies_ids[company_name] = [employee_id]

    elif employee_id not in dict_companies_ids[company_name]:
        dict_companies_ids[company_name].append(employee_id)
    company_id_data = input().split(" -> ")

for current_company, current_ids in dict_companies_ids.items():
    print(current_company)
    for person_id in current_ids:
        print(f"-- {person_id}")
