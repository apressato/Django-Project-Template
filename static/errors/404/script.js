/*
 * Copyright (c) 2020-2023 by APressato <apressato.oss@gmail.com>
 *
 * This file is part of Support_DashBoard.
 * Support_DashBoard is a website to help Support Teams in their work.
 *
 * Support_DashBoard is free software: you can redistribute it and/or modify
 * it under the terms of the
 * Creative Commons Attribution ShareAlike 4.0 International
 * as published by Creative Commons.
 *
 * Support_DashBoard is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY.  See the
 * Creative Commons Attribution ShareAlike 4.0 International for more details.
 *
 * You should have received a copy of the
 * Creative Commons Attribution ShareAlike 4.0 International
 * along with Support_DashBoard. If not,
 * see <https://creativecommons.org/licenses/by-sa/4.0/legalcode>.
 */

function type(n, t) {
    var str = document.getElementsByTagName("code")[n].innerHTML.toString();
    var i = 0;
    document.getElementsByTagName("code")[n].innerHTML = "";

    setTimeout(function() {
        var se = setInterval(function() {
            i++;
            document.getElementsByTagName("code")[n].innerHTML =
                str.slice(0, i) + "|";
            if (i == str.length) {
                clearInterval(se);
                document.getElementsByTagName("code")[n].innerHTML = str;
            }
        }, 10);
    }, t);
}

type(0, 0);
type(1, 600);
type(2, 1300);