def compare_strings(str1, str2):
    if type(str1) != str or type(str2) != str:
        return 0
    elif str1 == str2:
        return 1
    elif str2 == "learn":
        return 3
    elif len(str1) > len(str2):
        return 2
    else:
        return None
def main():

 print (compare_strings("hello", "hello"))
 print(compare_strings("python", "learn"))
 print(compare_strings("hello", "hi"))
print(compare_strings(10, "hello"))
print(compare_strings("hi", "hello"))
if __name__ == "__main__":
       main()