from django.shortcuts import redirect


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.role == "SA":
                return redirect("/account_requests/")
            elif request.user.role == "PH":
                return redirect("/account_requests/")
            elif request.user.role == "PA":
                return redirect("/account_requests/")
            else:
                return view_func(request, *args, **kwargs)
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func
