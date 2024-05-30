import beaker as bk
import pyteal as pt

class MyState:
    result = bk.GlobalStateValue(pt.TealType.uint64)    


app = bk.Application("Calculator", state=MyState())

@app.external
def add(a: pt.abi.Uint64, b: pt.abi.Uint64, *, output: pt.abi.Uint64) -> pt.Expr:
    add_result = a.get() + b.get()
    return pt.Seq()