#! /usr/bin/env python
#############################################################################
#
#              setup.py
#
# File:        $Source: /home/d/work/personal/ticker-cvs/epm/setup.py,v $
# Version:     $RCSfile: setup.py,v $ $Revision: 1.1 $
# Copyright:   (C) 2001, David Arnold.
#
# COPYRIGHT_BEGIN
#
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# * Redistributions of source code must retain the above
#   copyright notice, this list of conditions and the following
#   disclaimer.
#
# * Redistributions in binary form must reproduce the above
#   copyright notice, this list of conditions and the following
#   disclaimer in the documentation and/or other materials
#   provided with the distribution.
#
# * Neither the name of the DSTC nor the names
#   of its contributors may be used to endorse or promote
#   products derived from this software without specific prior
#   written permission. 
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# REGENTS OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# COPYRIGHT_END
#############################################################################

__revision__ = "$Revision: 1.1 $"[11:-2]

#############################################################################

from   distutils.core import setup

setup (name="epm",
       version="0.4",
       description="Elvin Presence Monitor",
       author="David Arnold",
       author_email="elvin@dstc.com",
       url="http://elvin.dstc.com/projects/ticker",
       licence="Copyright (C) David Arnold, 2001.",
       long_description="""This package provides a GTK application that implements the
       Elvin Presence Protocol, used to determine the availability and other
       information about users on a network.""",
       data_files = [("etc", ["epm.conf"]),
                     ],
       scripts = ["epm", "epmd"],
       )

#############################################################################
#  end of setup.py
