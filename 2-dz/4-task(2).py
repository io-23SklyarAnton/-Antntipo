import re


def unpack_ssgs(truck: list):
    result = ""
    counter = 1
    for box in truck:
        for product in box:
            ssg_packs = re.match(r"\[(?P<pack>(?P<ssg>.)(?P=ssg){3})]", product)
            if ssg_packs:
                if counter % 5:
                    result += (" ".join(ssg_packs.group("pack"))) + " "
                    counter += 1
                else:
                    counter = 1
    return result.strip()


print(unpack_ssgs([('[IlII]', '[llll]', '[1111]', '[@@@@]', '[||||]', '[║║║║]')]))