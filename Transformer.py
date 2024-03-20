import torch

class Transformer:

    def __init__(self):
        pass



    def attn_head_pass(self):
        q = torch.nn.matmul(self.att1.prev_layer_input, self.att1.q_lw)
        k = torch.nn.matmul(self.att1.prev_layer_input, self.att1.k_lw)
        v = torch.nn.matmul(self.att1.prev_layer_input, self.att1.v_lw)
        qk = torch.nn.matmul(q,k)
        qk_d = qk/self.k_lq.shape[1]
        mqkd = torch.masked_tensor(qk_d, self.att1.mask)
        mqkd_smx = torch.softmax(mqkd)
        self.attn.output = torch.nn.matmul(mqkd_smx, v)