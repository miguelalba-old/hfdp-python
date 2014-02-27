import ducks
import flybehaviors


mallard = ducks.MallardDuck()
mallard.quack()
mallard.fly()

model = ducks.ModelDuck()
model.fly()
model.set_fly_behavior(flybehaviors.FlyRocketPowered())
model.fly()
