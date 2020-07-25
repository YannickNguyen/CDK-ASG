#!/usr/bin/env python3

from aws_cdk import core

from bananatag.bananatag_stack import BananatagStack


app = core.App()
BananatagStack(app, "bananatag")

app.synth()
