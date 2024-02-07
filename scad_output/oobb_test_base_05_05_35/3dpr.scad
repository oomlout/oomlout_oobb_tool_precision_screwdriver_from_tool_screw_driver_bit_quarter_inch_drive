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
						translate(v = [0, 0, 17.7450000000]) {
							rotate_extrude(angle = 360) {
								translate(v = [5.5880000000, 0, 0]) {
									circle(r = 3.1750000000);
								}
							}
						}
					}
				}
			}
		}
	}
	union();
}