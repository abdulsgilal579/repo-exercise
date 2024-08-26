def hero(bullets, dragons):
    if bullets >= dragons*2:
        print("Person will survive")
    else:
        print("The person will not survice")
    if bullets - dragons*2 > 0:
        print(f"The person will dance because he has {bullets - dragons*2} bullets remaining.")
    

print(hero(7,2))

