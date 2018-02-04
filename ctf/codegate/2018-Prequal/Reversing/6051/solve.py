from angr import *

p = Project("./6051", load_options={'auto_load_libs': False})
ex = p.surveyors.Explorer(find=(0x0000000000000A24, ), avoid=(0x00000000000009FA,))
ex.run()

print("\"" + ex.found[0].state.posix.dumps(0) + "\"")
print(ex.found[0].state.posix.dumps(0).encode("hex"))