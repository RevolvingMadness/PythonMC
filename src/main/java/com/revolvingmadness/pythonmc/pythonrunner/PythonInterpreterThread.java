package com.revolvingmadness.pythonmc.pythonrunner;

import com.revolvingmadness.pythonmc.Mod;
import jep.JepConfig;
import jep.SubInterpreter;

import java.io.PrintStream;

public class PythonInterpreterThread extends Thread {
	public SubInterpreter interpreter;

	public PythonInterpreterThread() {
		JepConfig config = new JepConfig();
		config.addIncludePaths("C:/Users/USERNAME/IntelliJProjects/PythonMC/run");
		config.redirectStdout(new PrintStream(PythonExecutor.outputStream));
		config.redirectStdErr(new PrintStream(PythonExecutor.errorOutputStream));
		Mod.LOGGER.info("Starting interpreter PythonMC version " + Mod.pythonMCVersion);
		this.interpreter = new SubInterpreter(config);
	}

	@Override
	public void interrupt() {
		Mod.LOGGER.info("Stopping interpreter as player logged out");
		this.interpreter.close();
		super.interrupt();
	}
}
