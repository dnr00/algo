import beaker as bk
import pyteal as pt

app = bk.Application("Calculator")

@app.external
def add(a: pt.abi.Uint64, b: pt.abi.Uint64, *, output: pt.abi.Uint64) -> pt.Expr:
    add_result = a.get() + b.get()
    return output.set(add_result)