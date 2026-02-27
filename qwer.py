def solution(text, ending):
    return True if text[(len(text)-len(ending)):]==ending else False
print(solution("samurai", "ai" ))