h, m, sa = input().split(":")
h, s, isPM = int(h), int(sa[:2]), sa[2:] == "PM"
h += 12 if (isPM and h < 12) else (-12 if h is 12 and not isPM else 0)
print(":".join(map(lambda x: "{:02d}".format(x), [h, int(m), s])))
