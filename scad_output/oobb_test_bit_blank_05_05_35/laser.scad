$fn = 50;


difference() {
	union() {
		translate(v = [0, 0, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						linear_extrude(height = 26) {
							polygon(points = [[3.6658550000, 0.0000000000], [1.8329275000, 3.1747235566], [-1.8329275000, 3.1747235566], [-3.6658550000, 0.0000000000], [-1.8329275000, -3.1747235566], [1.8329275000, -3.1747235566]]);
						}
					}
					union() {
						translate(v = [0, 0, 17]) {
							rotate_extrude(angle = 360) {
								translate(v = [6.3500000000, 0, 0]) {
									circle(r = 3.9687500000);
								}
							}
						}
						difference() {
							cylinder(h = 2, r1 = 10.5000000000, r2 = 11.6750000000);
							cylinder(h = 2, r1 = 2.5000000000, r2 = 3.6750000000);
						}
					}
				}
			}
		}
	}
	union();
}