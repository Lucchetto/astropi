import time

class mario_running:
    def __init__(self, sense_hat):
        self.sense = sense_hat
    def mario_run_anim(self):
        frame_sleep = 0.1
        g = (129,118,158)
        r = (255, 0, 76)
        w = (255,255,255)
        bscuro = (21,43,93)
        bchiaro = (35,174,255)
        rosa = (255,203,169)
        marr = (171,82,48)
        e = (0,0,0)
        gial = (255,255,13)
        
        paxi = [
            e, e, e, r, r, r, w, e,
            e, e, e, r, r, r, r, r,
            e, e, marr, rosa, marr, e, rosa, e,
            e, e, marr, rosa, rosa, marr, marr, rosa,
            e, e, e, marr, rosa, rosa, rosa, e,
            e, r, r, gial, bchiaro, bchiaro, gial, e,
            w, e, bscuro, bchiaro, bchiaro, bchiaro, bscuro, w,
            e, e, marr, e, e, e, marr, e,
            ]

        self.sense.set_pixels(paxi)

        time.sleep(frame_sleep)

        paxi2 = [
            e, e, e, r, r, r, w, e,
            e, e, e, r, r, r, r, r,
            e, e, marr, rosa, marr, e, rosa, e,
            e, e, marr, rosa, rosa, marr, marr, rosa,
            e, e, e, marr, rosa, rosa, rosa, e,
            e, r, r, gial, bchiaro, gial, e, e,
            e, r, w, bscuro, bchiaro, bscuro, e, w,
            e, e, e, marr, e, marr, e, e,
           ]

        self.sense.set_pixels(paxi2)

        time.sleep(frame_sleep)

        paxi3 = [
            e, e, e, r, r, w, r, e,
            e, e, e, r, r, r, r, r,
            e, e, rosa, marr, e, rosa, e, e,
            e, e, rosa, rosa, marr, marr, rosa, marr,
            e, r, r, rosa, rosa, rosa, rosa, e,
            w, e, r, gial, bchiaro, bchiaro, gial, w,
            e, e, bscuro, bchiaro, bchiaro, bchiaro, bscuro, e,
            e, e, marr, e, e, e, marr, e,
            ]

        self.sense.set_pixels(paxi3)

        time.sleep(frame_sleep)

        paxi3 = [
            e, e, e, r, r, w, r, e,
            e, e, e, r, r, r, r, r,
            e, e, rosa, marr, e, rosa, e, e,
            e, e, rosa, rosa, marr, marr, rosa, marr,
            e, r, r, rosa, rosa, rosa, rosa, e,
            w, e, r, gial, bchiaro, bchiaro, gial, e,
            e, marr, bscuro, bchiaro, bchiaro, bchiaro, bchiaro, bscuro,
            e, e, e, e, e, e, e, marr,
            ]

        self.sense.set_pixels(paxi3)

        time.sleep(frame_sleep)

        paxi4 = [
            e, e, e, r, r, w, r, e,
            e, e, e, r, r, r, r, r,
            e, e, rosa, marr, e, rosa, e, e,
            e, e, rosa, rosa, marr, marr, rosa, marr,
            e, r, r, rosa, rosa, rosa, rosa, e,
            w, e, r, gial, bchiaro, bchiaro, gial, e,
            e, marr, bchiaro, bchiaro, bchiaro, bchiaro, bchiaro, bscuro,
            e, e, e, e, e, e, e, marr,
            ]

        self.sense.set_pixels(paxi4)

        time.sleep(frame_sleep)
