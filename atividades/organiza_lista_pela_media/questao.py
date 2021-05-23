# 2021-04-14, lucas.mayer.almeida@ccc.ufcg.edu.br
# A função coloca os valores menores que a média 
# nas primeiras posições da lista e os maiores que a média logo depois

def organiza_por_media(nums) :
    total = 0
    for i in nums :
        total += i
    if len(nums) == 0:
        return nums
    media = total / len(nums)
    for i in range(len(nums)) :
        j = i
        while j > 0 and nums[j] <= media and nums[j-1] > media :
            nums[j], nums[j-1] = nums[j-1], nums[j]
            j -= 1
    return nums
