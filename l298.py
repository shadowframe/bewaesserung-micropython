class DCMotor:
    def __init__(self, pin1, pin2, pin3, pin4, enable_l, enable_r, min_duty=750, max_duty=1023):
        self.pin1 = pin1
        self.pin2 = pin2
        self.pin3 = pin3
        self.pin4 = pin4
        self.enable_l = enable_l
        self.enable_r = enable_r
        self.min_duty = min_duty
        self.max_duty = max_duty

    def forward(self, speed):
        self.speed = speed
        self.enable_l.duty_u16(self.duty_cycle(self.speed))
        self.pin1.value(0)
        self.pin2.value(1)
        self.enable_r.duty_u16(self.duty_cycle(self.speed))
        self.pin3.value(0)
        self.pin4.value(1)

    def backwards(self, speed):
        self.speed = speed
        self.enable_l.duty_u16(self.duty_cycle(self.speed))
        self.pin1.value(1)
        self.pin2.value(0)
        self.enable_r.duty_u16(self.duty_cycle(self.speed))
        self.pin3.value(1)
        self.pin4.value(0)

    def stop(self):
        self.enable_l.duty_u16(0)
        self.enable_r.duty_u16(0)
        self.pin1.value(0)
        self.pin2.value(0)
        self.pin3.value(0)
        self.pin4.value(0)

    def left(self, speed):
        self.speed = speed
        self.enable_l.duty_u16(0)
        self.pin1.value(0)
        self.pin2.value(0)
        self.enable_r.duty_u16(self.duty_cycle(self.speed))
        self.pin3.value(0)
        self.pin4.value(1)

    def right(self, speed):
        self.speed = speed
        self.enable_l.duty_u16(self.duty_cycle(self.speed))
        self.pin1.value(0)
        self.pin2.value(1)
        self.enable_r.duty_u16(0)
        self.pin3.value(0)
        self.pin4.value(0)

    def duty_cycle(self, speed):
        if self.speed <= 0 or self.speed > 100:
            duty_cycle = 0
        else:
            duty_cycle = int(self.min_duty + (self.max_duty - self.min_duty) * ((self.speed - 1) / (100 - 1)))
            return duty_cycle

