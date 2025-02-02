$fn = 500;


difference() {
	union() {
		cylinder(h = 5, r1 = 2.1250000000, r2 = 4.7735000000);
		translate(v = [0, 0, 11.0000000000]) {
			cylinder(h = 59, r = 5.0000000000);
		}
		translate(v = [0, 0, 65.0000000000]) {
			cylinder(h = 30, r1 = 5.0000000000, r2 = 9.0000000000);
		}
		translate(v = [0, 0, 95.0000000000]) {
			cylinder(h = 5, r = 9.0000000000);
		}
		translate(v = [0, 0, 5]) {
			linear_extrude(height = 6) {
				polygon(points = [[5.7735000000, 0.0000000000], [2.8867500000, 4.9999976687], [-2.8867500000, 4.9999976687], [-5.7735000000, 0.0000000000], [-2.8867500000, -4.9999976687], [2.8867500000, -4.9999976687]]);
			}
		}
		translate(v = [0, 0, 25]) {
			linear_extrude(height = 9) {
				polygon(points = [[7.5055500000, 0.0000000000], [3.7527750000, 6.4999969694], [-3.7527750000, 6.4999969694], [-7.5055500000, 0.0000000000], [-3.7527750000, -6.4999969694], [3.7527750000, -6.4999969694]]);
			}
		}
	}
	union() {
		translate(v = [0, 0, 32]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [0.1000000000, 0, 0]) {
							#linear_extrude(height = 228.2000000000) {
								polygon(points = [[3.8658550000, 0.0000000000], [1.9329275000, 3.3479286373], [-1.9329275000, 3.3479286373], [-3.8658550000, 0.0000000000], [-1.9329275000, -3.3479286373], [1.9329275000, -3.3479286373]]);
							}
						}
						#translate(v = [0, 0, -121.8000000000]) {
							cylinder(h = 150, r = 2.2250000000);
						}
					}
					union() {
						difference() {
							#cylinder(h = 2, r1 = 10.2250000000, r2 = 11.7750000000);
							#cylinder(h = 2, r1 = 2.2250000000, r2 = 3.7750000000);
						}
					}
				}
			}
		}
		translate(v = [0, 0, 29.5000000000]) {
			rotate(a = [90, 30.0000000000, 0]) {
				difference() {
					union() {
						#linear_extrude(height = 3.2500000000) {
							polygon(points = [[3.4620000000, 0.0000000000], [1.7310000000, 2.9981799479], [-1.7310000000, 2.9981799479], [-3.4620000000, 0.0000000000], [-1.7310000000, -2.9981799479], [1.7310000000, -2.9981799479]]);
						}
					}
					union();
				}
			}
		}
		translate(v = [0, 0, 32.2500000000]) {
			rotate(a = [90, 30.0000000000, 0]) {
				difference() {
					union() {
						#linear_extrude(height = 3.2500000000) {
							polygon(points = [[3.4620000000, 0.0000000000], [1.7310000000, 2.9981799479], [-1.7310000000, 2.9981799479], [-3.4620000000, 0.0000000000], [-1.7310000000, -2.9981799479], [1.7310000000, -2.9981799479]]);
						}
					}
					union();
				}
			}
		}
		#translate(v = [0, 0, 29.5000000000]) {
			rotate(a = [90, 0, 0]) {
				cylinder(h = 12, r = 1.8000000000);
			}
		}
		translate(v = [0, 0, 16.0000000000]) {
			rotate_extrude(angle = 360) {
				translate(v = [26.5000000000, 0, 0]) {
					circle(r = 22.5000000000);
				}
			}
		}
		translate(v = [0, 0, 43.0000000000]) {
			rotate_extrude(angle = 360) {
				translate(v = [26.5000000000, 0, 0]) {
					circle(r = 22.5000000000);
				}
			}
		}
		translate(v = [0, 0, 60]) {
			rotate_extrude(angle = 360) {
				translate(v = [154.5000000000, 0, 0]) {
					circle(r = 150.0000000000);
				}
			}
		}
	}
}