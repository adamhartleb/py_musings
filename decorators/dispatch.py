from html import escape
from decimal import Decimal


def html_escape(arg):
    return escape(str(arg))


# def html_int(a):
#     return f'{a}(<i>{str(hex(a))}</i>)'


def html_real(a):
    return f'{round(a,2):.2f}'


def html_str(s):
    return html_escape(s).replace('\n', '<br/>\n')


def html_dict(d):
    items = (f'<li>{k}={v}</li>' for k, v in d.items())
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'


# def htmlize(arg):
#     if isinstance(arg, int):
#         return html_int(arg)
#     elif isinstance(arg, float) or isinstance(arg, Decimal):
#         return html_real(arg)
#     elif isinstance(arg, str):
#         return html_str(arg)
#     elif isinstance(arg, list) or isinstance(arg, tuple):
#         return html_list(arg)
#     elif isinstance(arg, dict):
#         return html_dict(arg)
#     else:
#         return html_escape(arg)

# def htmlize(arg):
#     registry = {
#         object: html_escape,
#         int: html_int,
#         float: html_int,
#         Decimal: html_int,
#         str: html_str,
#         list: html_list,
#         tuple: html_list,
#         dict: html_dict
#     }

#     fn = registry.get(type(arg), registry[object])

#     return fn(arg)


# def single_dispatch(fn):
#     registry = {}

#     registry[object] = fn

#     def inner(arg):
#         f = registry.get(type(arg), registry[object])
#         return f(arg)

#     return inner

def single_dispatch(fn):
    registry = {}

    registry[object] = fn

    def register(type_):
        def inner(fn):
            registry[type_] = fn
            return fn
        return inner

    def decorated(arg):
        return registry.get(type(arg), registry[object])(arg)

    decorated.register = register
    return decorated


@single_dispatch
def htmlize(a):
    return escape(str(a))


@htmlize.register(int)
def html_int(a):
    return f'{a}(<i>{str(hex(a))}</i>)'


@htmlize.register(tuple)
@htmlize.register(list)
def html_list(l):
    items = (f'<li>{html_escape(item)}</li>' for item in l)
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'


print(htmlize(100))
print(htmlize([1, 2, 3]))
