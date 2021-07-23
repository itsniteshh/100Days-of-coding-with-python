def build_profile(fname, lname, **usef_info):
    usef_info["first name"] = fname
    usef_info["last name"] = lname
    return usef_info

profile = build_profile("Nitesh", "Jha", hobby = "trying", gonna_make_it = "Yes")
print(profile)