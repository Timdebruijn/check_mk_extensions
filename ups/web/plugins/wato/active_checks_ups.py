#!/usr/bin/env python
# -*- encoding: utf-8; py-indent-offset: 4 -*-

#
# (c) 2013 Heinlein Support GmbH
#          Robert Sander <r.sander@heinlein-support.de>
#

# This is free software;  you can redistribute it and/or modify it
# under the  terms of the  GNU General Public License  as published by
# the Free Software Foundation in version 2.  This file is distributed
# in the hope that it will be useful, but WITHOUT ANY WARRANTY;  with-
# out even the implied warranty of  MERCHANTABILITY  or  FITNESS FOR A
# PARTICULAR PURPOSE. See the  GNU General Public License for more de-
# ails.  You should have  received  a copy of the  GNU  General Public
# License along with GNU Make; see the file  COPYING.  If  not,  write
# to the Free Software Foundation, Inc., 51 Franklin St,  Fifth Floor,
# Boston, MA 02110-1301 USA.

group = "activechecks"

register_rule(group,
              "active_checks:ups",
              Dictionary(
                  title = _("Check UPS"),
                  help = _("Checks UPS values"),
                  elements = [
                      ( "hostname",
                        TextAscii(title = _("DNS Hostname or IP address"),
                                  default_value = "$HOSTADDRESS$",
                                  ),
                        ),
                      ( "upsname",
                        TextAscii(title = _("UPS Name"),
                                  allow_empty = False,
                                  ),
                        ),
                      ( "port",
                        Integer(title = _("Port number"),
                                minvalue = 1,
                                maxvalue = 65535,
                                default_value = 3493,
                                ),
                        ),
                      ]
                  ),
              match = 'all'
              )

