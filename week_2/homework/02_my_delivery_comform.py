# Q. 배달의 민족 서버 개발자로 입사했다.
# 상점에서 현재 가능한 메뉴가 ["떡볶이", "만두", "오뎅", "사이다", "콜라"] 일 때, 
# 유저가 ["오뎅", "콜라", "만두"] 를 주문했다.

# 그렇다면, 현재 주문 가능한 상태인지 여부를 반환하시오.

shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "순대", "만두"]

# 정렬 이후에 해당 매뉴를 계속 찾기

def order_list(menus, order):
    shop_menus = menus
    shop_orders = order
    shop_menus.sort()
    for i in shop_orders:
        result = is_available_to_order(menus, i)
        if result == False:
            return False
    return True

def is_available_to_order(menus, target):
    # 리스트 저장 후 정렬
    
    #리스트 최소와 최대 값 지정
    max_count = len(menus)
    min_count = 0
    center_count = (max_count+min_count)//2

    while min_count <= max_count:
        center_count = (max_count+min_count)//2

        print(target, shop_menus[center_count],center_count)

        if shop_menus[center_count] < target :
            min_count = center_count +1

        elif shop_menus[center_count] > target:
            max_count = center_count -1

        else:
            return True

    return False


result = order_list(shop_menus, shop_orders)
print(result)