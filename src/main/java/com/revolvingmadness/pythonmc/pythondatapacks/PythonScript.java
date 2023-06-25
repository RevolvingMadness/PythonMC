package com.revolvingmadness.pythonmc.pythondatapacks;

import net.minecraft.resource.Resource;
import net.minecraft.util.Identifier;

import java.io.BufferedReader;
import java.io.IOException;
import java.util.Scanner;

public class PythonScript {
	Identifier id;
	String content;
	String namespace;
	String path;
	
	public PythonScript(Identifier id, String content, String namespace, String path) {
		this.id = id;
		this.content = content;
		this.namespace = namespace;
		this.path = path;
	}
	
	public static String readFromResource(Resource resource) {
		BufferedReader reader;
		try {
			reader = resource.getReader();
		} catch (IOException e) {
			e.printStackTrace();
			return null;
		}
		Scanner scanner = new Scanner(reader);
		StringBuilder content = new StringBuilder();
		while (scanner.hasNextLine()) {
			content.append(scanner.nextLine());
			content.append("\n");
		}
		return content.toString();
	}
}
