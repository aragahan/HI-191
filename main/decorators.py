from django.shortcuts import redirect


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.role == "SA":
                return redirect("/account_requests/")
            elif request.user.role == "PH":
                return redirect("")
            else:
                return redirect("")
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func
