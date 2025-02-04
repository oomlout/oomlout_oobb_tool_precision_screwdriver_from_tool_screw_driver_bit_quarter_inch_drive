$fn = 50;


difference() {
	union() {
		cylinder(h = 3, r1 = 2.1250000000, r2 = 4.7735000000);
		translate(v = [0, 0, 9.0000000000]) {
			cylinder(h = 51, r = 5.0000000000);
		}
		translate(v = [0, 0, 55.0000000000]) {
			cylinder(h = 35, r1 = 5.0000000000, r2 = 9.0000000000);
		}
		translate(v = [0, 0, 90.0000000000]) {
			cylinder(h = 5, r = 9.0000000000);
		}
		translate(v = [0, 0, 3]) {
			linear_extrude(height = 6) {
				polygon(points = [[5.7735000000, 0.0000000000], [2.8867500000, 4.9999976687], [-2.8867500000, 4.9999976687], [-5.7735000000, 0.0000000000], [-2.8867500000, -4.9999976687], [2.8867500000, -4.9999976687]]);
			}
		}
		translate(v = [0, 0, 50]) {
			linear_extrude(height = 9) {
				polygon(points = [[7.5055500000, 0.0000000000], [3.7527750000, 6.4999969694], [-3.7527750000, 6.4999969694], [-7.5055500000, 0.0000000000], [-3.7527750000, -6.4999969694], [3.7527750000, -6.4999969694]]);
			}
		}
	}
	union() {
		translate(v = [0, 0, 64]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [0.1000000000, 0, 0]) {
							#linear_extrude(height = 228.2000000000) {
								polygon(points = [[3.8658550000, 0.0000000000], [1.9329275000, 3.3479286373], [-1.9329275000, 3.3479286373], [-3.8658550000, 0.0000000000], [-1.9329275000, -3.3479286373], [1.9329275000, -3.3479286373]]);
							}
						}
						#translate(v = [0, 0, -121.8000000000]) {
							cylinder(h = 150, r = 1.7250000000);
						}
					}
					union() {
						difference() {
							#cylinder(h = 2, r1 = 9.7250000000, r2 = 11.7750000000);
							#cylinder(h = 2, r1 = 1.7250000000, r2 = 3.7750000000);
						}
					}
				}
			}
		}
		translate(v = [0, 0, 54.5000000000]) {
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
		translate(v = [0, 0, 54.5000000000]) {
			rotate(a = [90, 30.0000000000, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -1.2500000000]) {
							#linear_extrude(height = 2.5000000000) {
								polygon(points = [[3.4620000000, 0.0000000000], [1.7310000000, 2.9981799479], [-1.7310000000, 2.9981799479], [-3.4620000000, 0.0000000000], [-1.7310000000, -2.9981799479], [1.7310000000, -2.9981799479]]);
							}
						}
					}
					union();
				}
			}
		}
		translate(v = [0, 0, 57.5000000000]) {
			rotate(a = [90, 30.0000000000, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -1.2500000000]) {
							#linear_extrude(height = 2.5000000000) {
								polygon(points = [[3.4620000000, 0.0000000000], [1.7310000000, 2.9981799479], [-1.7310000000, 2.9981799479], [-3.4620000000, 0.0000000000], [-1.7310000000, -2.9981799479], [1.7310000000, -2.9981799479]]);
							}
						}
					}
					union();
				}
			}
		}
		translate(v = [0, 0, 60.5000000000]) {
			rotate(a = [90, 30.0000000000, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -1.2500000000]) {
							#linear_extrude(height = 2.5000000000) {
								polygon(points = [[3.4620000000, 0.0000000000], [1.7310000000, 2.9981799479], [-1.7310000000, 2.9981799479], [-3.4620000000, 0.0000000000], [-1.7310000000, -2.9981799479], [1.7310000000, -2.9981799479]]);
							}
						}
					}
					union();
				}
			}
		}
		translate(v = [0, 0, 63.5000000000]) {
			rotate(a = [90, 30.0000000000, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -1.2500000000]) {
							#linear_extrude(height = 2.5000000000) {
								polygon(points = [[3.4620000000, 0.0000000000], [1.7310000000, 2.9981799479], [-1.7310000000, 2.9981799479], [-3.4620000000, 0.0000000000], [-1.7310000000, -2.9981799479], [1.7310000000, -2.9981799479]]);
							}
						}
					}
					union();
				}
			}
		}
		translate(v = [0, 0, 66.5000000000]) {
			rotate(a = [90, 30.0000000000, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -1.2500000000]) {
							#linear_extrude(height = 2.5000000000) {
								polygon(points = [[3.4620000000, 0.0000000000], [1.7310000000, 2.9981799479], [-1.7310000000, 2.9981799479], [-3.4620000000, 0.0000000000], [-1.7310000000, -2.9981799479], [1.7310000000, -2.9981799479]]);
							}
						}
					}
					union();
				}
			}
		}
		translate(v = [0, 0, 69.5000000000]) {
			rotate(a = [90, 30.0000000000, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -1.2500000000]) {
							#linear_extrude(height = 2.5000000000) {
								polygon(points = [[3.4620000000, 0.0000000000], [1.7310000000, 2.9981799479], [-1.7310000000, 2.9981799479], [-3.4620000000, 0.0000000000], [-1.7310000000, -2.9981799479], [1.7310000000, -2.9981799479]]);
							}
						}
					}
					union();
				}
			}
		}
		translate(v = [0, 0, 72.5000000000]) {
			rotate(a = [90, 30.0000000000, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -1.2500000000]) {
							#linear_extrude(height = 2.5000000000) {
								polygon(points = [[3.4620000000, 0.0000000000], [1.7310000000, 2.9981799479], [-1.7310000000, 2.9981799479], [-3.4620000000, 0.0000000000], [-1.7310000000, -2.9981799479], [1.7310000000, -2.9981799479]]);
							}
						}
					}
					union();
				}
			}
		}
		translate(v = [0, 0, 75.5000000000]) {
			rotate(a = [90, 30.0000000000, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -1.2500000000]) {
							#linear_extrude(height = 2.5000000000) {
								polygon(points = [[3.4620000000, 0.0000000000], [1.7310000000, 2.9981799479], [-1.7310000000, 2.9981799479], [-3.4620000000, 0.0000000000], [-1.7310000000, -2.9981799479], [1.7310000000, -2.9981799479]]);
							}
						}
					}
					union();
				}
			}
		}
		translate(v = [0, 0, 78.5000000000]) {
			rotate(a = [90, 30.0000000000, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -1.2500000000]) {
							#linear_extrude(height = 2.5000000000) {
								polygon(points = [[3.4620000000, 0.0000000000], [1.7310000000, 2.9981799479], [-1.7310000000, 2.9981799479], [-3.4620000000, 0.0000000000], [-1.7310000000, -2.9981799479], [1.7310000000, -2.9981799479]]);
							}
						}
					}
					union();
				}
			}
		}
		translate(v = [0, 0, 81.5000000000]) {
			rotate(a = [90, 30.0000000000, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -1.2500000000]) {
							#linear_extrude(height = 2.5000000000) {
								polygon(points = [[3.4620000000, 0.0000000000], [1.7310000000, 2.9981799479], [-1.7310000000, 2.9981799479], [-3.4620000000, 0.0000000000], [-1.7310000000, -2.9981799479], [1.7310000000, -2.9981799479]]);
							}
						}
					}
					union();
				}
			}
		}
		translate(v = [0, 0, 84.5000000000]) {
			rotate(a = [90, 30.0000000000, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -1.2500000000]) {
							#linear_extrude(height = 2.5000000000) {
								polygon(points = [[3.4620000000, 0.0000000000], [1.7310000000, 2.9981799479], [-1.7310000000, 2.9981799479], [-3.4620000000, 0.0000000000], [-1.7310000000, -2.9981799479], [1.7310000000, -2.9981799479]]);
							}
						}
					}
					union();
				}
			}
		}
		translate(v = [0, 0, 87.5000000000]) {
			rotate(a = [90, 30.0000000000, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -1.2500000000]) {
							#linear_extrude(height = 2.5000000000) {
								polygon(points = [[3.4620000000, 0.0000000000], [1.7310000000, 2.9981799479], [-1.7310000000, 2.9981799479], [-3.4620000000, 0.0000000000], [-1.7310000000, -2.9981799479], [1.7310000000, -2.9981799479]]);
							}
						}
					}
					union();
				}
			}
		}
		translate(v = [0, 0, 90.5000000000]) {
			rotate(a = [90, 30.0000000000, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -1.2500000000]) {
							#linear_extrude(height = 2.5000000000) {
								polygon(points = [[3.4620000000, 0.0000000000], [1.7310000000, 2.9981799479], [-1.7310000000, 2.9981799479], [-3.4620000000, 0.0000000000], [-1.7310000000, -2.9981799479], [1.7310000000, -2.9981799479]]);
							}
						}
					}
					union();
				}
			}
		}
		translate(v = [0, 0, 93.5000000000]) {
			rotate(a = [90, 30.0000000000, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -1.2500000000]) {
							#linear_extrude(height = 2.5000000000) {
								polygon(points = [[3.4620000000, 0.0000000000], [1.7310000000, 2.9981799479], [-1.7310000000, 2.9981799479], [-3.4620000000, 0.0000000000], [-1.7310000000, -2.9981799479], [1.7310000000, -2.9981799479]]);
							}
						}
					}
					union();
				}
			}
		}
		translate(v = [0, 0, 96.5000000000]) {
			rotate(a = [90, 30.0000000000, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -1.2500000000]) {
							#linear_extrude(height = 2.5000000000) {
								polygon(points = [[3.4620000000, 0.0000000000], [1.7310000000, 2.9981799479], [-1.7310000000, 2.9981799479], [-3.4620000000, 0.0000000000], [-1.7310000000, -2.9981799479], [1.7310000000, -2.9981799479]]);
							}
						}
					}
					union();
				}
			}
		}
		translate(v = [0, 0, 99.5000000000]) {
			rotate(a = [90, 30.0000000000, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -1.2500000000]) {
							#linear_extrude(height = 2.5000000000) {
								polygon(points = [[3.4620000000, 0.0000000000], [1.7310000000, 2.9981799479], [-1.7310000000, 2.9981799479], [-3.4620000000, 0.0000000000], [-1.7310000000, -2.9981799479], [1.7310000000, -2.9981799479]]);
							}
						}
					}
					union();
				}
			}
		}
		translate(v = [0, 0, 102.5000000000]) {
			rotate(a = [90, 30.0000000000, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -1.2500000000]) {
							#linear_extrude(height = 2.5000000000) {
								polygon(points = [[3.4620000000, 0.0000000000], [1.7310000000, 2.9981799479], [-1.7310000000, 2.9981799479], [-3.4620000000, 0.0000000000], [-1.7310000000, -2.9981799479], [1.7310000000, -2.9981799479]]);
							}
						}
					}
					union();
				}
			}
		}
		translate(v = [0, 0, 105.5000000000]) {
			rotate(a = [90, 30.0000000000, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -1.2500000000]) {
							#linear_extrude(height = 2.5000000000) {
								polygon(points = [[3.4620000000, 0.0000000000], [1.7310000000, 2.9981799479], [-1.7310000000, 2.9981799479], [-3.4620000000, 0.0000000000], [-1.7310000000, -2.9981799479], [1.7310000000, -2.9981799479]]);
							}
						}
					}
					union();
				}
			}
		}
		translate(v = [0, 0, 108.5000000000]) {
			rotate(a = [90, 30.0000000000, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -1.2500000000]) {
							#linear_extrude(height = 2.5000000000) {
								polygon(points = [[3.4620000000, 0.0000000000], [1.7310000000, 2.9981799479], [-1.7310000000, 2.9981799479], [-3.4620000000, 0.0000000000], [-1.7310000000, -2.9981799479], [1.7310000000, -2.9981799479]]);
							}
						}
					}
					union();
				}
			}
		}
		translate(v = [0, 0, 111.5000000000]) {
			rotate(a = [90, 30.0000000000, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -1.2500000000]) {
							#linear_extrude(height = 2.5000000000) {
								polygon(points = [[3.4620000000, 0.0000000000], [1.7310000000, 2.9981799479], [-1.7310000000, 2.9981799479], [-3.4620000000, 0.0000000000], [-1.7310000000, -2.9981799479], [1.7310000000, -2.9981799479]]);
							}
						}
					}
					union();
				}
			}
		}
		translate(v = [0, 0, 114.5000000000]) {
			rotate(a = [90, 30.0000000000, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -1.2500000000]) {
							#linear_extrude(height = 2.5000000000) {
								polygon(points = [[3.4620000000, 0.0000000000], [1.7310000000, 2.9981799479], [-1.7310000000, 2.9981799479], [-3.4620000000, 0.0000000000], [-1.7310000000, -2.9981799479], [1.7310000000, -2.9981799479]]);
							}
						}
					}
					union();
				}
			}
		}
		translate(v = [0, 0, 117.5000000000]) {
			rotate(a = [90, 30.0000000000, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -1.2500000000]) {
							#linear_extrude(height = 2.5000000000) {
								polygon(points = [[3.4620000000, 0.0000000000], [1.7310000000, 2.9981799479], [-1.7310000000, 2.9981799479], [-3.4620000000, 0.0000000000], [-1.7310000000, -2.9981799479], [1.7310000000, -2.9981799479]]);
							}
						}
					}
					union();
				}
			}
		}
		translate(v = [0, 0, 120.5000000000]) {
			rotate(a = [90, 30.0000000000, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -1.2500000000]) {
							#linear_extrude(height = 2.5000000000) {
								polygon(points = [[3.4620000000, 0.0000000000], [1.7310000000, 2.9981799479], [-1.7310000000, 2.9981799479], [-3.4620000000, 0.0000000000], [-1.7310000000, -2.9981799479], [1.7310000000, -2.9981799479]]);
							}
						}
					}
					union();
				}
			}
		}
		translate(v = [0, 0, 123.5000000000]) {
			rotate(a = [90, 30.0000000000, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -1.2500000000]) {
							#linear_extrude(height = 2.5000000000) {
								polygon(points = [[3.4620000000, 0.0000000000], [1.7310000000, 2.9981799479], [-1.7310000000, 2.9981799479], [-3.4620000000, 0.0000000000], [-1.7310000000, -2.9981799479], [1.7310000000, -2.9981799479]]);
							}
						}
					}
					union();
				}
			}
		}
		translate(v = [0, 0, 126.5000000000]) {
			rotate(a = [90, 30.0000000000, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -1.2500000000]) {
							#linear_extrude(height = 2.5000000000) {
								polygon(points = [[3.4620000000, 0.0000000000], [1.7310000000, 2.9981799479], [-1.7310000000, 2.9981799479], [-3.4620000000, 0.0000000000], [-1.7310000000, -2.9981799479], [1.7310000000, -2.9981799479]]);
							}
						}
					}
					union();
				}
			}
		}
		translate(v = [0, 0, 129.5000000000]) {
			rotate(a = [90, 30.0000000000, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -1.2500000000]) {
							#linear_extrude(height = 2.5000000000) {
								polygon(points = [[3.4620000000, 0.0000000000], [1.7310000000, 2.9981799479], [-1.7310000000, 2.9981799479], [-3.4620000000, 0.0000000000], [-1.7310000000, -2.9981799479], [1.7310000000, -2.9981799479]]);
							}
						}
					}
					union();
				}
			}
		}
		translate(v = [0, 0, 132.5000000000]) {
			rotate(a = [90, 30.0000000000, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -1.2500000000]) {
							#linear_extrude(height = 2.5000000000) {
								polygon(points = [[3.4620000000, 0.0000000000], [1.7310000000, 2.9981799479], [-1.7310000000, 2.9981799479], [-3.4620000000, 0.0000000000], [-1.7310000000, -2.9981799479], [1.7310000000, -2.9981799479]]);
							}
						}
					}
					union();
				}
			}
		}
		translate(v = [0, 0, 135.5000000000]) {
			rotate(a = [90, 30.0000000000, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -1.2500000000]) {
							#linear_extrude(height = 2.5000000000) {
								polygon(points = [[3.4620000000, 0.0000000000], [1.7310000000, 2.9981799479], [-1.7310000000, 2.9981799479], [-3.4620000000, 0.0000000000], [-1.7310000000, -2.9981799479], [1.7310000000, -2.9981799479]]);
							}
						}
					}
					union();
				}
			}
		}
		translate(v = [0, 0, 138.5000000000]) {
			rotate(a = [90, 30.0000000000, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -1.2500000000]) {
							#linear_extrude(height = 2.5000000000) {
								polygon(points = [[3.4620000000, 0.0000000000], [1.7310000000, 2.9981799479], [-1.7310000000, 2.9981799479], [-3.4620000000, 0.0000000000], [-1.7310000000, -2.9981799479], [1.7310000000, -2.9981799479]]);
							}
						}
					}
					union();
				}
			}
		}
		translate(v = [0, 0, 141.5000000000]) {
			rotate(a = [90, 30.0000000000, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -1.2500000000]) {
							#linear_extrude(height = 2.5000000000) {
								polygon(points = [[3.4620000000, 0.0000000000], [1.7310000000, 2.9981799479], [-1.7310000000, 2.9981799479], [-3.4620000000, 0.0000000000], [-1.7310000000, -2.9981799479], [1.7310000000, -2.9981799479]]);
							}
						}
					}
					union();
				}
			}
		}
		rotate(a = [0, 0, 0.0000000000]) {
			translate(v = [9.5000000000, 0, 0]) {
				translate(v = [-0.5000000000, -0.5000000000, 90.0000000000]) {
					rotate(a = [0, 0, 45]) {
						cube(size = [1, 1, 5]);
					}
				}
			}
		}
		rotate(a = [0, 0, 10.0000000000]) {
			translate(v = [9.5000000000, 0, 0]) {
				translate(v = [-0.5000000000, -0.5000000000, 90.0000000000]) {
					rotate(a = [0, 0, 45]) {
						cube(size = [1, 1, 5]);
					}
				}
			}
		}
		rotate(a = [0, 0, 20.0000000000]) {
			translate(v = [9.5000000000, 0, 0]) {
				translate(v = [-0.5000000000, -0.5000000000, 90.0000000000]) {
					rotate(a = [0, 0, 45]) {
						cube(size = [1, 1, 5]);
					}
				}
			}
		}
		rotate(a = [0, 0, 30.0000000000]) {
			translate(v = [9.5000000000, 0, 0]) {
				translate(v = [-0.5000000000, -0.5000000000, 90.0000000000]) {
					rotate(a = [0, 0, 45]) {
						cube(size = [1, 1, 5]);
					}
				}
			}
		}
		rotate(a = [0, 0, 40.0000000000]) {
			translate(v = [9.5000000000, 0, 0]) {
				translate(v = [-0.5000000000, -0.5000000000, 90.0000000000]) {
					rotate(a = [0, 0, 45]) {
						cube(size = [1, 1, 5]);
					}
				}
			}
		}
		rotate(a = [0, 0, 50.0000000000]) {
			translate(v = [9.5000000000, 0, 0]) {
				translate(v = [-0.5000000000, -0.5000000000, 90.0000000000]) {
					rotate(a = [0, 0, 45]) {
						cube(size = [1, 1, 5]);
					}
				}
			}
		}
		rotate(a = [0, 0, 60.0000000000]) {
			translate(v = [9.5000000000, 0, 0]) {
				translate(v = [-0.5000000000, -0.5000000000, 90.0000000000]) {
					rotate(a = [0, 0, 45]) {
						cube(size = [1, 1, 5]);
					}
				}
			}
		}
		rotate(a = [0, 0, 70.0000000000]) {
			translate(v = [9.5000000000, 0, 0]) {
				translate(v = [-0.5000000000, -0.5000000000, 90.0000000000]) {
					rotate(a = [0, 0, 45]) {
						cube(size = [1, 1, 5]);
					}
				}
			}
		}
		rotate(a = [0, 0, 80.0000000000]) {
			translate(v = [9.5000000000, 0, 0]) {
				translate(v = [-0.5000000000, -0.5000000000, 90.0000000000]) {
					rotate(a = [0, 0, 45]) {
						cube(size = [1, 1, 5]);
					}
				}
			}
		}
		rotate(a = [0, 0, 90.0000000000]) {
			translate(v = [9.5000000000, 0, 0]) {
				translate(v = [-0.5000000000, -0.5000000000, 90.0000000000]) {
					rotate(a = [0, 0, 45]) {
						cube(size = [1, 1, 5]);
					}
				}
			}
		}
		rotate(a = [0, 0, 100.0000000000]) {
			translate(v = [9.5000000000, 0, 0]) {
				translate(v = [-0.5000000000, -0.5000000000, 90.0000000000]) {
					rotate(a = [0, 0, 45]) {
						cube(size = [1, 1, 5]);
					}
				}
			}
		}
		rotate(a = [0, 0, 110.0000000000]) {
			translate(v = [9.5000000000, 0, 0]) {
				translate(v = [-0.5000000000, -0.5000000000, 90.0000000000]) {
					rotate(a = [0, 0, 45]) {
						cube(size = [1, 1, 5]);
					}
				}
			}
		}
		rotate(a = [0, 0, 120.0000000000]) {
			translate(v = [9.5000000000, 0, 0]) {
				translate(v = [-0.5000000000, -0.5000000000, 90.0000000000]) {
					rotate(a = [0, 0, 45]) {
						cube(size = [1, 1, 5]);
					}
				}
			}
		}
		rotate(a = [0, 0, 130.0000000000]) {
			translate(v = [9.5000000000, 0, 0]) {
				translate(v = [-0.5000000000, -0.5000000000, 90.0000000000]) {
					rotate(a = [0, 0, 45]) {
						cube(size = [1, 1, 5]);
					}
				}
			}
		}
		rotate(a = [0, 0, 140.0000000000]) {
			translate(v = [9.5000000000, 0, 0]) {
				translate(v = [-0.5000000000, -0.5000000000, 90.0000000000]) {
					rotate(a = [0, 0, 45]) {
						cube(size = [1, 1, 5]);
					}
				}
			}
		}
		rotate(a = [0, 0, 150.0000000000]) {
			translate(v = [9.5000000000, 0, 0]) {
				translate(v = [-0.5000000000, -0.5000000000, 90.0000000000]) {
					rotate(a = [0, 0, 45]) {
						cube(size = [1, 1, 5]);
					}
				}
			}
		}
		rotate(a = [0, 0, 160.0000000000]) {
			translate(v = [9.5000000000, 0, 0]) {
				translate(v = [-0.5000000000, -0.5000000000, 90.0000000000]) {
					rotate(a = [0, 0, 45]) {
						cube(size = [1, 1, 5]);
					}
				}
			}
		}
		rotate(a = [0, 0, 170.0000000000]) {
			translate(v = [9.5000000000, 0, 0]) {
				translate(v = [-0.5000000000, -0.5000000000, 90.0000000000]) {
					rotate(a = [0, 0, 45]) {
						cube(size = [1, 1, 5]);
					}
				}
			}
		}
		rotate(a = [0, 0, 180.0000000000]) {
			translate(v = [9.5000000000, 0, 0]) {
				translate(v = [-0.5000000000, -0.5000000000, 90.0000000000]) {
					rotate(a = [0, 0, 45]) {
						cube(size = [1, 1, 5]);
					}
				}
			}
		}
		rotate(a = [0, 0, 190.0000000000]) {
			translate(v = [9.5000000000, 0, 0]) {
				translate(v = [-0.5000000000, -0.5000000000, 90.0000000000]) {
					rotate(a = [0, 0, 45]) {
						cube(size = [1, 1, 5]);
					}
				}
			}
		}
		rotate(a = [0, 0, 200.0000000000]) {
			translate(v = [9.5000000000, 0, 0]) {
				translate(v = [-0.5000000000, -0.5000000000, 90.0000000000]) {
					rotate(a = [0, 0, 45]) {
						cube(size = [1, 1, 5]);
					}
				}
			}
		}
		rotate(a = [0, 0, 210.0000000000]) {
			translate(v = [9.5000000000, 0, 0]) {
				translate(v = [-0.5000000000, -0.5000000000, 90.0000000000]) {
					rotate(a = [0, 0, 45]) {
						cube(size = [1, 1, 5]);
					}
				}
			}
		}
		rotate(a = [0, 0, 220.0000000000]) {
			translate(v = [9.5000000000, 0, 0]) {
				translate(v = [-0.5000000000, -0.5000000000, 90.0000000000]) {
					rotate(a = [0, 0, 45]) {
						cube(size = [1, 1, 5]);
					}
				}
			}
		}
		rotate(a = [0, 0, 230.0000000000]) {
			translate(v = [9.5000000000, 0, 0]) {
				translate(v = [-0.5000000000, -0.5000000000, 90.0000000000]) {
					rotate(a = [0, 0, 45]) {
						cube(size = [1, 1, 5]);
					}
				}
			}
		}
		rotate(a = [0, 0, 240.0000000000]) {
			translate(v = [9.5000000000, 0, 0]) {
				translate(v = [-0.5000000000, -0.5000000000, 90.0000000000]) {
					rotate(a = [0, 0, 45]) {
						cube(size = [1, 1, 5]);
					}
				}
			}
		}
		rotate(a = [0, 0, 250.0000000000]) {
			translate(v = [9.5000000000, 0, 0]) {
				translate(v = [-0.5000000000, -0.5000000000, 90.0000000000]) {
					rotate(a = [0, 0, 45]) {
						cube(size = [1, 1, 5]);
					}
				}
			}
		}
		rotate(a = [0, 0, 260.0000000000]) {
			translate(v = [9.5000000000, 0, 0]) {
				translate(v = [-0.5000000000, -0.5000000000, 90.0000000000]) {
					rotate(a = [0, 0, 45]) {
						cube(size = [1, 1, 5]);
					}
				}
			}
		}
		rotate(a = [0, 0, 270.0000000000]) {
			translate(v = [9.5000000000, 0, 0]) {
				translate(v = [-0.5000000000, -0.5000000000, 90.0000000000]) {
					rotate(a = [0, 0, 45]) {
						cube(size = [1, 1, 5]);
					}
				}
			}
		}
		rotate(a = [0, 0, 280.0000000000]) {
			translate(v = [9.5000000000, 0, 0]) {
				translate(v = [-0.5000000000, -0.5000000000, 90.0000000000]) {
					rotate(a = [0, 0, 45]) {
						cube(size = [1, 1, 5]);
					}
				}
			}
		}
		rotate(a = [0, 0, 290.0000000000]) {
			translate(v = [9.5000000000, 0, 0]) {
				translate(v = [-0.5000000000, -0.5000000000, 90.0000000000]) {
					rotate(a = [0, 0, 45]) {
						cube(size = [1, 1, 5]);
					}
				}
			}
		}
		rotate(a = [0, 0, 300.0000000000]) {
			translate(v = [9.5000000000, 0, 0]) {
				translate(v = [-0.5000000000, -0.5000000000, 90.0000000000]) {
					rotate(a = [0, 0, 45]) {
						cube(size = [1, 1, 5]);
					}
				}
			}
		}
		rotate(a = [0, 0, 310.0000000000]) {
			translate(v = [9.5000000000, 0, 0]) {
				translate(v = [-0.5000000000, -0.5000000000, 90.0000000000]) {
					rotate(a = [0, 0, 45]) {
						cube(size = [1, 1, 5]);
					}
				}
			}
		}
		rotate(a = [0, 0, 320.0000000000]) {
			translate(v = [9.5000000000, 0, 0]) {
				translate(v = [-0.5000000000, -0.5000000000, 90.0000000000]) {
					rotate(a = [0, 0, 45]) {
						cube(size = [1, 1, 5]);
					}
				}
			}
		}
		rotate(a = [0, 0, 330.0000000000]) {
			translate(v = [9.5000000000, 0, 0]) {
				translate(v = [-0.5000000000, -0.5000000000, 90.0000000000]) {
					rotate(a = [0, 0, 45]) {
						cube(size = [1, 1, 5]);
					}
				}
			}
		}
		rotate(a = [0, 0, 340.0000000000]) {
			translate(v = [9.5000000000, 0, 0]) {
				translate(v = [-0.5000000000, -0.5000000000, 90.0000000000]) {
					rotate(a = [0, 0, 45]) {
						cube(size = [1, 1, 5]);
					}
				}
			}
		}
		rotate(a = [0, 0, 350.0000000000]) {
			translate(v = [9.5000000000, 0, 0]) {
				translate(v = [-0.5000000000, -0.5000000000, 90.0000000000]) {
					rotate(a = [0, 0, 45]) {
						cube(size = [1, 1, 5]);
					}
				}
			}
		}
		#translate(v = [0, 0, 54.5000000000]) {
			rotate(a = [90, 0, 0]) {
				cylinder(h = 12, r = 1.8000000000);
			}
		}
		translate(v = [0, 0, 33.1000000000]) {
			rotate_extrude(angle = 360) {
				translate(v = [79.0000000000, 0, 0]) {
					circle(r = 75.0000000000);
				}
			}
		}
		translate(v = [0, 0, 31.3000000000]) {
			rotate_extrude(angle = 360) {
				translate(v = [79.0000000000, 0, 0]) {
					circle(r = 75.0000000000);
				}
			}
		}
		translate(v = [0, 0, 27.7000000000]) {
			rotate_extrude(angle = 360) {
				translate(v = [79.0000000000, 0, 0]) {
					circle(r = 75.0000000000);
				}
			}
		}
		translate(v = [0, 0, 25.9000000000]) {
			rotate_extrude(angle = 360) {
				translate(v = [79.0000000000, 0, 0]) {
					circle(r = 75.0000000000);
				}
			}
		}
		translate(v = [0, 0, 69.2500000000]) {
			rotate_extrude(angle = 360) {
				translate(v = [80.5000000000, 0, 0]) {
					circle(r = 75.0000000000);
				}
			}
		}
		translate(v = [0, 0, 79.5000000000]) {
			rotate_extrude(angle = 360) {
				translate(v = [15.0000000000, 0, 0]) {
					circle(r = 8.0000000000);
				}
			}
		}
		rotate(a = [0, 0, 0.0000000000]) {
			translate(v = [0, 0, 0]) {
				translate(v = [81.0000000000, 0, 29.5000000000]) {
					rotate(a = [90, 0, 0]) {
						rotate_extrude(angle = 360) {
							translate(v = [76.2500000000, 0, 0]) {
								circle(r = 1.2500000000);
							}
						}
					}
				}
			}
		}
		rotate(a = [0, 0, 60.0000000000]) {
			translate(v = [0, 0, 0]) {
				translate(v = [81.0000000000, 0, 29.5000000000]) {
					rotate(a = [90, 0, 0]) {
						rotate_extrude(angle = 360) {
							translate(v = [76.2500000000, 0, 0]) {
								circle(r = 1.2500000000);
							}
						}
					}
				}
			}
		}
		rotate(a = [0, 0, 120.0000000000]) {
			translate(v = [0, 0, 0]) {
				translate(v = [81.0000000000, 0, 29.5000000000]) {
					rotate(a = [90, 0, 0]) {
						rotate_extrude(angle = 360) {
							translate(v = [76.2500000000, 0, 0]) {
								circle(r = 1.2500000000);
							}
						}
					}
				}
			}
		}
		rotate(a = [0, 0, 180.0000000000]) {
			translate(v = [0, 0, 0]) {
				translate(v = [81.0000000000, 0, 29.5000000000]) {
					rotate(a = [90, 0, 0]) {
						rotate_extrude(angle = 360) {
							translate(v = [76.2500000000, 0, 0]) {
								circle(r = 1.2500000000);
							}
						}
					}
				}
			}
		}
		rotate(a = [0, 0, 240.0000000000]) {
			translate(v = [0, 0, 0]) {
				translate(v = [81.0000000000, 0, 29.5000000000]) {
					rotate(a = [90, 0, 0]) {
						rotate_extrude(angle = 360) {
							translate(v = [76.2500000000, 0, 0]) {
								circle(r = 1.2500000000);
							}
						}
					}
				}
			}
		}
		rotate(a = [0, 0, 300.0000000000]) {
			translate(v = [0, 0, 0]) {
				translate(v = [81.0000000000, 0, 29.5000000000]) {
					rotate(a = [90, 0, 0]) {
						rotate_extrude(angle = 360) {
							translate(v = [76.2500000000, 0, 0]) {
								circle(r = 1.2500000000);
							}
						}
					}
				}
			}
		}
	}
}