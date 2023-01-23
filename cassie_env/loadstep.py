import numpy as np
import random


class CassieTrajectory:
    def __init__(self, filepath):
        n = 1 + 35 + 32 + 10 + 10 + 10
        data = np.fromfile(filepath, dtype=np.double).reshape((-1, n))
        self.time = data[:, 0]
        self.qpos = data[:, 1:36]
        self.qvel = data[:, 36:68]
        self.torque = data[:, 68:78]
        self.mpos = data[:, 78:88]
        self.mvel = data[:, 88:98]

    def state(self, t):
        tmax = self.time[-1]
        i = int((t % tmax) / tmax * len(self.time))
        return (self.qpos[i], self.qvel[i])

    def action(self, t):
        tmax = self.time[-1]
        i = int((t % tmax) / tmax * len(self.time))
        return (self.mpos[i], self.mvel[i], self.torque[i])

    def sample(self):
        i = random.randrange(len(self.time))
        return (self.time[i], self.qpos[i], self.qvel[i])
"""
import numpy as np
tr = CassieTrajectory("trajectory/stepdata.bin")
time_colume = np.expand_dims(np.array(range(len(tr.mpos))), 1)
mpos = tr.mpos #[:, [2, 3, 4, 7, 8, 9]]
mpos[:, -1] *=-1
mpos[:, -6] *=-1
mpos = mpos[np.linspace(0, 1681, 110).astype(int)]
mpos = np.concatenate((mpos, (-1.5)*np.ones((mpos.shape[0], 2))), axis=1)
njit_pos = np.loadtxt("/home/shuzhen/Documents/cassie_rl_env/NJIT_walking.mot")

pos = np.concatenate((njit_pos[:, :8], mpos), axis=1)
np.savetxt("/home/shuzhen/Documents/cassie_rl_env/NJIT_cassie_walking_tmp.mot", pos, delimiter='   ', fmt='%.5f')

with open("/home/shuzhen/Bipedal_robot_walking_test_Cassie/data/motion/NJIT_BME_tmp_walking_motion.mot", "r") as f:
    lines = f.readlines()[:8]
    lines[4] = lines[4].replace("18", "20")
    lines[-1] = "time root_joint_q1 root_joint_q2 root_joint_q3 root_joint_q4 root_joint_q5 root_joint_q6 root_joint_q7" \
                " hip_rotation_left hip_abduction_left hip_flexion_left knee_joint_left ankle_joint_left" \
                " hip_rotation_right hip_abduction_right hip_flexion_right knee_joint_right ankle_joint_right toe_joint_left toe_joint_right\n"
#print(lines)
with open("/home/shuzhen/Bipedal_robot_walking_test_Cassie/data/motion/NJIT_cassie_walking.mot", "w") as f:
    f.writelines(lines)
    lines = open("/home/shuzhen/Documents/cassie_rl_env/NJIT_cassie_walking_tmp.mot", "r").readlines()
    lines[-1] = lines[-1].strip()
    f.writelines(lines)
"""

