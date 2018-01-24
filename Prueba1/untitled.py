from PySSC import PySSC
if __name__ == "__main__":
	ssc = PySSC()
	print ('Current folder = /home/miguel/Desktop/Python_files/SAM examples/Prueba1')
	print ('SSC Version = ', ssc.version())
	print ('SSC Build Information = ', ssc.build_info().decode("utf - 8"))
	ssc.module_exec_set_print(0)
	data = ssc.data_create()
	ssc.data_set_string( data, b'file_name', b'/home/miguel/SAM/2017.9.5/solar_resource/USA CA Imperial (TMY3).csv' );
	ssc.data_set_number( data, b'I_bn_des', 950 )
	ssc.data_set_number( data, b'T_cold_ref', 100 )
	ssc.data_set_number( data, b'P_turb_des', 20 )
	ssc.data_set_number( data, b'T_hot', 393 )
	ssc.data_set_number( data, b'x_b_des', 0.75 )
	ssc.data_set_number( data, b'q_pb_des', 5 )
	ssc.data_set_number( data, b'fP_hdr_c', 0.0099999997764825821 )
	ssc.data_set_number( data, b'fP_sf_boil', 0.075000002980232239 )
	ssc.data_set_number( data, b'fP_hdr_h', 0.02500000037252903 )
	ssc.data_set_number( data, b'nModBoil', 6 )
	ssc.data_set_number( data, b'nLoops', 3 )
	ssc.data_set_number( data, b'eta_pump', 0.85000002384185791 )
	ssc.data_set_number( data, b'theta_stow', 10 )
	ssc.data_set_number( data, b'theta_dep', 10 )
	ssc.data_set_number( data, b'T_fp', 10 )
	ssc.data_set_number( data, b'Pipe_hl_coef', 0.0035000001080334187 )
	ssc.data_set_number( data, b'SCA_drives_elec', 0.20000000298023224 )
	ssc.data_set_number( data, b'ColAz', 0 )
	ssc.data_set_number( data, b'e_startup', 2.7000000476837158 )
	ssc.data_set_number( data, b'T_amb_des_sf', 42 )
	ssc.data_set_number( data, b'V_wind_max', 20 )
	ssc.data_set_number( data, b'csp.lf.sf.water_per_wash', 0.019999999552965164 )
	ssc.data_set_number( data, b'csp.lf.sf.washes_per_year', 12 )
	A_aperture = [[ 513.5999755859375 ], [ 0 ]];
	ssc.data_set_matrix( data, b'A_aperture', A_aperture );
	L_col = [[ 44.799999237060547 ], [ 0 ]];
	ssc.data_set_matrix( data, b'L_col', L_col );
	OptCharType = [[ 1 ], [ 0 ]];
	ssc.data_set_matrix( data, b'OptCharType', OptCharType );
	IAM_T = [[ 0.98960000276565552,   0.043999999761581421,   -0.072099998593330383,   -0.23270000517368317,   0 ], [ 0,   0,   0,   0,   0 ]];
	ssc.data_set_matrix( data, b'IAM_T', IAM_T );
	IAM_L = [[ 1.0031000375747681,   -0.22589999437332153,   0.53680002689361572,   -1.6433999538421631,   0.72219997644424438 ], [ 0,   0,   0,   0,   0 ]];
	ssc.data_set_matrix( data, b'IAM_L', IAM_L );
	TrackingError = [[ 1 ], [ 0 ]];
	ssc.data_set_matrix( data, b'TrackingError', TrackingError );
	GeomEffects = [[ 0.8399999737739563 ], [ 0 ]];
	ssc.data_set_matrix( data, b'GeomEffects', GeomEffects );
	rho_mirror_clean = [[ 0.93500000238418579 ], [ 0 ]];
	ssc.data_set_matrix( data, b'rho_mirror_clean', rho_mirror_clean );
	dirt_mirror = [[ 0.94999998807907104 ], [ 0 ]];
	ssc.data_set_matrix( data, b'dirt_mirror', dirt_mirror );
	error = [[ 1 ], [ 0 ]];
	ssc.data_set_matrix( data, b'error', error );
	HLCharType = [[ 1 ], [ 0 ]];
	ssc.data_set_matrix( data, b'HLCharType', HLCharType );
	HL_dT = [[ 0,   0.67199999094009399,   0.0025559999048709869,   0,   0 ], [ 0,   0,   0,   0,   0 ]];
	ssc.data_set_matrix( data, b'HL_dT', HL_dT );
	HL_W = [[ 1,   0,   0,   0,   0 ], [ 0,   0,   0,   0,   0 ]];
	ssc.data_set_matrix( data, b'HL_W', HL_W );
	D_2 = [[ 0.065999999642372131 ], [ 0 ]];
	ssc.data_set_matrix( data, b'D_2', D_2 );
	D_3 = [[ 0.070000000298023224 ], [ 0 ]];
	ssc.data_set_matrix( data, b'D_3', D_3 );
	D_4 = [[ 0.11500000208616257 ], [ 0 ]];
	ssc.data_set_matrix( data, b'D_4', D_4 );
	D_5 = [[ 0.11999999731779099 ], [ 0 ]];
	ssc.data_set_matrix( data, b'D_5', D_5 );
	D_p = [[ 0 ], [ 0 ]];
	ssc.data_set_matrix( data, b'D_p', D_p );
	Rough = [[ 4.5000000682193786e-05 ], [ 0 ]];
	ssc.data_set_matrix( data, b'Rough', Rough );
	Flow_type = [[ 1 ], [ 0 ]];
	ssc.data_set_matrix( data, b'Flow_type', Flow_type );
	AbsorberMaterial = [[ 1 ], [ 0 ]];
	ssc.data_set_matrix( data, b'AbsorberMaterial', AbsorberMaterial );
	HCE_FieldFrac = [[ 0.98500001430511475,   0.0099999997764825821,   0.004999999888241291,   0 ], [ 0,   0,   0,   0 ]];
	ssc.data_set_matrix( data, b'HCE_FieldFrac', HCE_FieldFrac );
	alpha_abs = [[ 0.95999997854232788,   0.95999997854232788,   0.80000001192092896,   0 ], [ 0,   0,   0,   0 ]];
	ssc.data_set_matrix( data, b'alpha_abs', alpha_abs );
	b_eps_HCE1 = [[ 0 ], [ 0.13840000331401825 ]];
	ssc.data_set_matrix( data, b'b_eps_HCE1', b_eps_HCE1 );
	b_eps_HCE2 = [[ 0 ], [ 0.64999997615814209 ]];
	ssc.data_set_matrix( data, b'b_eps_HCE2', b_eps_HCE2 );
	b_eps_HCE3 = [[ 0 ], [ 0.64999997615814209 ]];
	ssc.data_set_matrix( data, b'b_eps_HCE3', b_eps_HCE3 );
	b_eps_HCE4 = [[ 0 ], [ 0.13840000331401825 ]];
	ssc.data_set_matrix( data, b'b_eps_HCE4', b_eps_HCE4 );
	sh_eps_HCE1 = [[ 0 ], [ 0 ]];
	ssc.data_set_matrix( data, b'sh_eps_HCE1', sh_eps_HCE1 );
	sh_eps_HCE2 = [[ 0 ], [ 0 ]];
	ssc.data_set_matrix( data, b'sh_eps_HCE2', sh_eps_HCE2 );
	sh_eps_HCE3 = [[ 0 ], [ 0 ]];
	ssc.data_set_matrix( data, b'sh_eps_HCE3', sh_eps_HCE3 );
	sh_eps_HCE4 = [[ 0 ], [ 0 ]];
	ssc.data_set_matrix( data, b'sh_eps_HCE4', sh_eps_HCE4 );
	alpha_env = [[ 0.019999999552965164,   0.019999999552965164,   0,   0 ], [ 0,   0,   0,   0 ]];
	ssc.data_set_matrix( data, b'alpha_env', alpha_env );
	EPSILON_4 = [[ 0.86000001430511475,   0.86000001430511475,   1,   0 ], [ 0,   0,   0,   0 ]];
	ssc.data_set_matrix( data, b'EPSILON_4', EPSILON_4 );
	Tau_envelope = [[ 0.96299999952316284,   0.96299999952316284,   1,   0 ], [ 0,   0,   0,   0 ]];
	ssc.data_set_matrix( data, b'Tau_envelope', Tau_envelope );
	GlazingIntactIn = [[ 1,   1,   0,   1 ], [ 0,   0,   0,   0 ]];
	ssc.data_set_matrix( data, b'GlazingIntactIn', GlazingIntactIn );
	AnnulusGas = [[ 1,   1,   1,   1 ], [ 0,   0,   0,   0 ]];
	ssc.data_set_matrix( data, b'AnnulusGas', AnnulusGas );
	P_a = [[ 9.9999997473787516e-05,   750,   750,   0 ], [ 0,   0,   0,   0 ]];
	ssc.data_set_matrix( data, b'P_a', P_a );
	Design_loss = [[ 150,   1100,   1500,   0 ], [ 0,   0,   0,   0 ]];
	ssc.data_set_matrix( data, b'Design_loss', Design_loss );
	Shadowing = [[ 0.95999997854232788,   0.95999997854232788,   0.95999997854232788,   0 ], [ 0,   0,   0,   0 ]];
	ssc.data_set_matrix( data, b'Shadowing', Shadowing );
	Dirt_HCE = [[ 0.98000001907348633,   0.98000001907348633,   1,   0 ], [ 0,   0,   0,   0 ]];
	ssc.data_set_matrix( data, b'Dirt_HCE', Dirt_HCE );
	b_OpticalTable = [[ -180,   -160,   -140,   -120,   -100,   -80,   -60,   -40,   -20,   0,   20,   40,   60,   80,   100,   120,   140,   160,   180,   -999.9000244140625 ], [ 0,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1 ], [ 10,   0.98000001907348633,   0.97444498538970947,   0.97197598218917847,   0.97284698486328125,   0.97690999507904053,   0.97690999507904053,   0.97284698486328125,   0.97197598218917847,   0.97444498538970947,   0.98000001907348633,   0.97444498538970947,   0.97197598218917847,   0.97284698486328125,   0.97690999507904053,   0.97690999507904053,   0.97284698486328125,   0.97197598218917847,   0.97444498538970947,   0.98000001907348633 ], [ 20,   0.93000000715255737,   0.92297601699829102,   0.92892998456954956,   0.94600498676300049,   0.95401901006698608,   0.95401901006698608,   0.94600498676300049,   0.92892998456954956,   0.92297601699829102,   0.93000000715255737,   0.92297601699829102,   0.92892998456954956,   0.94600498676300049,   0.95401901006698608,   0.95401901006698608,   0.94600498676300049,   0.92892998456954956,   0.92297601699829102,   0.93000000715255737 ], [ 30,   0.8399999737739563,   0.83861798048019409,   0.87069100141525269,   0.9130210280418396,   0.94091099500656128,   0.94091099500656128,   0.9130210280418396,   0.87069100141525269,   0.83861798048019409,   0.8399999737739563,   0.83861798048019409,   0.87069100141525269,   0.9130210280418396,   0.94091099500656128,   0.94091099500656128,   0.9130210280418396,   0.87069100141525269,   0.83861798048019409,   0.8399999737739563 ], [ 40,   0.72000002861022949,   0.72994697093963623,   0.80368697643280029,   0.86696100234985352,   0.90003901720046997,   0.90003901720046997,   0.86696100234985352,   0.80368697643280029,   0.72994697093963623,   0.72000002861022949,   0.72994697093963623,   0.80368697643280029,   0.86696100234985352,   0.90003901720046997,   0.90003901720046997,   0.86696100234985352,   0.80368697643280029,   0.72994697093963623,   0.72000002861022949 ], [ 50,   0.55000001192092896,   0.59125500917434692,   0.70745402574539185,   0.79350900650024414,   0.83955997228622437,   0.83955997228622437,   0.79350900650024414,   0.70745402574539185,   0.59125500917434692,   0.55000001192092896,   0.59125500917434692,   0.70745402574539185,   0.79350900650024414,   0.83955997228622437,   0.83955997228622437,   0.79350900650024414,   0.70745402574539185,   0.59125500917434692,   0.55000001192092896 ], [ 60,   0.34000000357627869,   0.43217799067497253,   0.59747797250747681,   0.66400599479675293,   0.69351100921630859,   0.69351100921630859,   0.66400599479675293,   0.59747797250747681,   0.43217799067497253,   0.34000000357627869,   0.43217799067497253,   0.59747797250747681,   0.66400599479675293,   0.69351100921630859,   0.69351100921630859,   0.66400599479675293,   0.59747797250747681,   0.43217799067497253,   0.34000000357627869 ], [ 70,   0.12999999523162842,   0.26525399088859558,   0.42558598518371582,   0.46449598670005798,   0.4771060049533844,   0.4771060049533844,   0.46449598670005798,   0.42558598518371582,   0.26525399088859558,   0.12999999523162842,   0.26525399088859558,   0.42558598518371582,   0.46449598670005798,   0.4771060049533844,   0.4771060049533844,   0.46449598670005798,   0.42558598518371582,   0.26525399088859558,   0.12999999523162842 ], [ 80,   0.0099999997764825821,   0.11369399726390839,   0.20891000330448151,   0.23325499892234802,   0.23882800340652466,   0.23882800340652466,   0.23325499892234802,   0.20891000330448151,   0.11369399726390839,   0.0099999997764825821,   0.11369399726390839,   0.20891000330448151,   0.23325499892234802,   0.23882800340652466,   0.23882800340652466,   0.23325499892234802,   0.20891000330448151,   0.11369399726390839,   0.0099999997764825821 ], [ 90,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0 ]];
	ssc.data_set_matrix( data, b'b_OpticalTable', b_OpticalTable );
	sh_OpticalTable = [[ 0,   0 ], [ 0,   0 ]];
	ssc.data_set_matrix( data, b'sh_OpticalTable', sh_OpticalTable );
	ssc.data_set_number( data, b'heat_sink_dP_frac', 0.0099999997764825821 )
	ssc.data_set_number( data, b'adjust:constant', 4 )
	module = ssc.module_create(b'linear_fresnel_dsg_iph')	
	ssc.module_exec_set_print( 0 );
	if ssc.module_exec(module, data) == 0:
		print ('linear_fresnel_dsg_iph simulation error')
		idx = 1
		msg = ssc.module_log(module, 0)
		while (msg != None):
			print ('	: ' + msg.decode("utf - 8"))
			msg = ssc.module_log(module, idx)
			idx = idx + 1
		SystemExit( "Simulation Error" );
	ssc.module_free(module)
	annual_energy = ssc.data_get_number(data, b'annual_energy');
	print ('Annual energy (year 1) = ', annual_energy)
	annual_field_energy = ssc.data_get_number(data, b'annual_field_energy');
	print ('Annual field energy (year 1) = ', annual_field_energy)
	annual_thermal_consumption = ssc.data_get_number(data, b'annual_thermal_consumption');
	print ('Annual thermal freeze protection (year 1) = ', annual_thermal_consumption)
	annual_electricity_consumption = ssc.data_get_number(data, b'annual_electricity_consumption');
	print ('Annual electricity load (year 1) = ', annual_electricity_consumption)
	ssc.data_free(data);