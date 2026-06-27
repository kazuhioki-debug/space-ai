import datetime
import rebound
from astropy.time import Time

print("====================================")
print("  ちきゅうぼうえいAIシステム 起動！")
print("====================================")

# NASAのデータから、大接近する小惑星「アポフィス」を呼び出す
sim = rebound.Simulation()
sim.units = ("yr", "AU", "Msun")
sim.add("Sun")
sim.add("Earth")
sim.add("Apophis")

# 2029年の大接近のとき、どれくらい近づくか計算する
sim.integrate(3.0)  # 3年後の宇宙へタイムワープ！

earth = sim.particles[1]
apophis = sim.particles[2]
dx, dy, dz = apophis.x - earth.x, apophis.y - earth.y, apophis.z - earth.z
kyori_km = (dx**2 + dy**2 + dz**2) ** 0.5 * 149597870.7

print(f"【計算結果】2029年、アポフィスは地球から約 {kyori_km:,.0f} km まで近づきます！")
print("※ 人工衛星よりも近いところを通るけど、地球にはぶつかりません。安全です！")
print("====================================")
