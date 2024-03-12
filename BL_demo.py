# ========================================================================
# Perceptual Quality Assessment of Smartphone Photography
# PyTorch Version 1.0 by Hanwei Zhu
# Copyright(c) 2020 Yuming Fang, Hanwei Zhu, Yan Zeng, Kede Ma, and Zhou Wang
# All Rights Reserved.
#
# ----------------------------------------------------------------------
# Permission to use, copy, or modify this software and its documentation
# for educational and research purposes only and without fee is hereby
# granted, provided that this copyright notice and the original authors'
# names appear on all copies and supporting documentation. This program
# shall not be used, rewritten, or adapted as the basis of a commercial
# software or hardware product without first obtaining permission of the
# authors. The authors make no representations about the suitability of
# this software for any purpose. It is provided "as is" without express
# or implied warranty.
# ----------------------------------------------------------------------
# This is an implementation of Baseline (BL) models for blind image
# quality assessment.
# Please refer to the following paper:
#
# Y. Fang et al., "Perceptual Quality Assessment of Smartphone Photography" 
# in IEEE Conference on Computer Vision and Pattern Recognition, 2020
#
# Kindly report any suggestions or corrections to hanwei.zhu@outlook.com
# ========================================================================

import torch
import torch.nn as nn
import torchvision
from Prepare_image import Image_load
from PIL import Image
import argparse
import os

class Baseline(nn.Module):
	def __init__(self):
		super(Baseline, self).__init__()
		self.backbone = torchvision.models.resnet50(pretrained=False)
		fc_feature = self.backbone.fc.in_features
		self.backbone.fc = nn.Linear(fc_feature, 1, bias=True)

	def forward(self, x):
		result = self.backbone(x)
		return result

class Demo(object):
	def __init__(self, load_weights=True, checkpoint_dir='./weights/BL_release.pt'):
		self.imgpath = ""
		self.load_weights = load_weights
		self.checkpoint_dir = checkpoint_dir

		self.prepare_image = Image_load(size=512, stride=224)

		self.model = Baseline()
		self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
		self.model.to(self.device)
		self.model_name = type(self.model).__name__

		if self.load_weights:
			self.initialize()

	def predit_quality(self):
		image_1 = self.prepare_image(Image.open(self.imgpath).convert("RGB"))
		# image_2 = self.prepare_image(Image.open(self.config.image_2).convert("RGB"))

		image_1 = image_1.to(self.device)
		self.model.eval()
		score_1 = self.model(image_1).mean()
		print(score_1.item())
		# image_2 = image_2.to(self.device)
		# score_2 = self.model(image_2).mean()
		# print(score_2.item())
		return score_1

	def initialize(self):
		ckpt_path = self.checkpoint_dir
		could_load = self._load_checkpoint(ckpt_path)
		if could_load:
			print('Checkpoint load successfully!')
		else:
			raise IOError('Fail to load the pretrained model')

	def _load_checkpoint(self, ckpt):
		if os.path.isfile(ckpt):
			print("[*] loading checkpoint '{}'".format(ckpt))
			checkpoint = torch.load(ckpt,map_location=torch.device('cpu'))
			self.model.load_state_dict(checkpoint['state_dict'])
			return True
		else:
			return False
	def get_image(self,imagepath):
		self.imgpath = imagepath



def parse_config():
	parser = argparse.ArgumentParser()
	parser.add_argument('--image_1', type=str, default='./images/05293.png')
	# parser.add_argument('--image_2', type=str, default='./images/00914.png')
	return parser.parse_args()

if __name__ == '__main__':
	image_path = './images/05293.png'
	demo = Demo(image_path)
	demo.predit_quality()

		









