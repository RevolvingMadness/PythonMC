package com.revolvingmadness.pythonmc.pythonrunner;

import com.revolvingmadness.pythonmc.Mod;
import jep.Interpreter;
import jep.JepConfig;
import jep.SubInterpreter;
import net.minecraft.server.command.ServerCommandSource;

import java.io.PrintStream;

public class PythonExecutorThread extends Thread {
	ServerCommandSource source;
	String namespace;
	String path;
	String content;
	JepConfig config;
	Interpreter interpreter;

	public PythonExecutorThread(ServerCommandSource source, String namespace, String path, String content) {
		this.source = source;
		this.namespace = namespace;
		this.path = path;
		this.content = content;

		JepConfig config = new JepConfig();
		config.addIncludePaths(System.getenv("HOME") + "/IntelliJProjects/PythonMC/run");
		config.redirectStdout(new PrintStream(PythonExecutor.outputStream));
		config.redirectStdErr(new PrintStream(PythonExecutor.errorOutputStream));
		this.config = config;
	}

	@Override
	public void run() {
		Mod.LOGGER.info("Starting interpreter PythonMC version " + Mod.pythonMCVersion);
		this.interpreter = new SubInterpreter(this.config);
		PythonExecutor.execute(this.source, this.namespace, this.path, this.content, this.interpreter);

		this.interrupt();
		this.interpreter.close();
	}
}
